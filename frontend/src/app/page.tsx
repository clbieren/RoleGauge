'use client';

import { useState, useEffect } from 'react';
import { RoleInfo, AnalyzeResponse, fetchRoles, analyzeProfile } from '@/lib/api';
import { useLocale } from '@/lib/useLocale';
import { initLocale } from '@/lib/i18n';
import { SAMPLE_ANALYSIS } from '@/lib/sampleAnalysis';

import AnalysisProgress from '@/components/AnalysisProgress';
import ResultsDashboard from '@/components/ResultsDashboard';
import AuthModal from '@/components/AuthModal';

import LandingNav from '@/components/landing/LandingNav';
import HeroSection from '@/components/landing/HeroSection';
import HowItWorks from '@/components/landing/HowItWorks';
import WhatWeAnalyze from '@/components/landing/WhatWeAnalyze';
import EvidenceSection from '@/components/landing/EvidenceSection';
import RoleComparison from '@/components/landing/RoleComparison';
import MissingSkills from '@/components/landing/MissingSkills';
import SampleAnalysisSection from '@/components/landing/SampleAnalysisSection';
import PersonasSection from '@/components/landing/PersonasSection';
import TrustSection from '@/components/landing/TrustSection';
import FinalCTA from '@/components/landing/FinalCTA';
import LandingFooter from '@/components/landing/LandingFooter';

import { useAuth } from '@/context/AuthContext';
import styles from './page.module.css';

type AppState = 'input' | 'analyzing' | 'results';

export default function HomePage() {
  const { locale, toggle, t } = useLocale();
  const { token } = useAuth();
  const [state, setState] = useState<AppState>('input');
  const [roles, setRoles] = useState<RoleInfo[]>([]);
  const [username, setUsername] = useState('');
  const [selectedRole, setSelectedRole] = useState('');
  const [selectedLevel, setSelectedLevel] = useState<'junior' | 'mid' | 'senior'>('mid');
  const [githubToken, setGithubToken] = useState('');
  const [showToken, setShowToken] = useState(false);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [error, setError] = useState('');
  const [analysisStep, setAnalysisStep] = useState(0);
  const [isHydrated, setIsHydrated] = useState(false);

  useEffect(() => {
    initLocale();
    fetchRoles().then(setRoles);

    // Restore last analysis result or saved username across page refreshes
    const timer = setTimeout(() => {
      try {
        const savedUser = localStorage.getItem('skilllens_username');
        if (savedUser) setUsername(savedUser);

        const savedResult = localStorage.getItem('skilllens_last_result');
        if (savedResult) {
          const parsed = JSON.parse(savedResult);
          if (parsed && parsed.id && parsed.skills) {
            setResult(parsed);
            setState('results');
            if (parsed.github_username) setUsername(parsed.github_username);
            if (parsed.role_id) setSelectedRole(parsed.role_id);
            if (parsed.level) setSelectedLevel(parsed.level);
          }
        }
      } catch {
        // ignore
      } finally {
        setIsHydrated(true);
      }
    }, 0);

    return () => clearTimeout(timer);
  }, []);

  const STEPS = [
    t('loadingStep1'),
    t('loadingStep2'),
    t('loadingStep3'),
    t('loadingStep4'),
    t('loadingStep5'),
  ];

  const handleAnalyze = async () => {
    if ((!username.trim() && !uploadedFile) || !selectedRole) return;

    setState('analyzing');
    setError('');
    setAnalysisStep(0);

    // Step progression timer
    let step = 0;
    const stepIntervals = [800, 1400, 1800, 1000];
    const timers: ReturnType<typeof setTimeout>[] = [];

    stepIntervals.forEach((delay, i) => {
      const accumulated = stepIntervals.slice(0, i + 1).reduce((a, b) => a + b, 0);
      const timer = setTimeout(() => {
        step = i + 1;
        setAnalysisStep(step);
      }, accumulated);
      timers.push(timer);
    });

    try {
      let response: AnalyzeResponse;
      if (uploadedFile) {
        const formData = new FormData();
        formData.append('role_id', selectedRole);
        formData.append('level', selectedLevel);
        if (username.trim()) formData.append('github_username', username.trim());
        if (githubToken) formData.append('github_token', githubToken);
        formData.append('file', uploadedFile);
        formData.append('use_ai', 'false');
        response = await analyzeProfile(formData, token || undefined);
      } else {
        response = await analyzeProfile({
          github_username: username.trim(),
          role_id: selectedRole,
          level: selectedLevel,
          github_token: githubToken || undefined,
          use_ai: false,
        }, token || undefined);
      }

      // Clear pending timers
      timers.forEach(clearTimeout);
      setAnalysisStep(5);

      setTimeout(() => {
        setResult(response);
        setState('results');
        if (typeof window !== 'undefined' && response.id) {
          window.history.pushState(null, '', `/results/${response.id}`);
        }
        try {
          if (username.trim()) localStorage.setItem('skilllens_username', username);
          localStorage.setItem('skilllens_last_result', JSON.stringify(response));
        } catch {
          // ignore
        }
      }, 400);
    } catch (err) {
      timers.forEach(clearTimeout);
      setError(err instanceof Error ? err.message : t('errorGeneral'));
      setState('input');
    }
  };

  const handleViewSample = () => {
    setResult(SAMPLE_ANALYSIS);
    setState('results');
  };

  const scrollToFormAndFocus = () => {
    const el = document.getElementById('hero-section');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      setTimeout(() => {
        const input = document.getElementById('hero-github-input');
        if (input) {
          (input as HTMLInputElement).focus();
        }
      }, 400);
    }
  };

  const handleReset = () => {
    setState('input');
    setResult(null);
    setAnalysisStep(0);
    setError('');
    if (typeof window !== 'undefined') {
      window.history.pushState(null, '', '/');
    }
    try {
      localStorage.removeItem('skilllens_last_result');
    } catch {
      // ignore
    }
  };

  const selectedRoleInfo = roles.find(r => r.role_id === selectedRole);

  if (!isHydrated) {
    return <div style={{ minHeight: '100vh', background: 'var(--bg-base)' }} />;
  }

  return (
    <>
      {state === 'input' && (
        <div className={styles.page}>
          <LandingNav
            locale={locale}
            toggleLocale={toggle}
            t={t}
            onLogoClick={() => setState('input')}
          />

          <main>
            <HeroSection
              username={username}
              setUsername={setUsername}
              selectedRole={selectedRole}
              setSelectedRole={setSelectedRole}
              selectedLevel={selectedLevel}
              setSelectedLevel={setSelectedLevel}
              githubToken={githubToken}
              setGithubToken={setGithubToken}
              showToken={showToken}
              setShowToken={setShowToken}
              uploadedFile={uploadedFile}
              setUploadedFile={setUploadedFile}
              roles={roles}
              error={error}
              onAnalyze={handleAnalyze}
              onViewSample={handleViewSample}
              t={t}
              locale={locale}
            />

            <HowItWorks t={t} />
            <WhatWeAnalyze t={t} />
            <EvidenceSection t={t} />
            <RoleComparison t={t} />
            <MissingSkills t={t} />
            <SampleAnalysisSection t={t} onViewSample={handleViewSample} />
            <PersonasSection t={t} />
            <TrustSection t={t} />
            <FinalCTA
              t={t}
              onStartAnalysis={scrollToFormAndFocus}
              onViewSample={handleViewSample}
            />
          </main>

          <LandingFooter t={t} />
        </div>
      )}

      {state === 'analyzing' && (
        <AnalysisProgress
          currentStep={analysisStep}
          steps={STEPS}
          username={username || uploadedFile?.name || 'Candidate'}
          roleName={
            selectedRoleInfo
              ? selectedRoleInfo.title.replace(/^(Junior|Mid|Senior)\s+/i, '')
              : selectedRole
          }
          level={selectedLevel}
          locale={locale}
        />
      )}

      {state === 'results' && result && (
        <ResultsDashboard
          result={result}
          onReset={handleReset}
        />
      )}

      <AuthModal locale={locale} />
    </>
  );
}
