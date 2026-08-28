'use client';

import { useState, useEffect } from 'react';
import { RoleInfo, AnalyzeResponse, fetchRoles, analyzeProfile } from '@/lib/api';
import GitHubInput from '@/components/GitHubInput';
import RoleSelector from '@/components/RoleSelector';
import AnalysisProgress from '@/components/AnalysisProgress';
import ResultsDashboard from '@/components/ResultsDashboard';
import styles from './page.module.css';

type AppState = 'input' | 'analyzing' | 'results';

export default function HomePage() {
  const [state, setState] = useState<AppState>('input');
  const [roles, setRoles] = useState<RoleInfo[]>([]);
  const [username, setUsername] = useState('');
  const [selectedRole, setSelectedRole] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('junior');
  const [githubToken, setGithubToken] = useState('');
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [error, setError] = useState('');
  const [progress, setProgress] = useState(0);
  const [progressMessage, setProgressMessage] = useState('');

  useEffect(() => {
    fetchRoles()
      .then(setRoles)
      .catch(() => setRoles([]));
  }, []);

  const handleAnalyze = async () => {
    if (!username.trim() || !selectedRole) return;

    setState('analyzing');
    setError('');
    setProgress(0);
    setProgressMessage('GitHub repolar taranıyor...');

    // Simulate progress
    const progressInterval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 0.9) {
          clearInterval(progressInterval);
          return 0.9;
        }
        const step = prev < 0.3 ? 0.05 : prev < 0.6 ? 0.03 : 0.01;
        const newProgress = prev + step;

        if (newProgress > 0.25 && prev <= 0.25) setProgressMessage('Dosya yapıları analiz ediliyor...');
        if (newProgress > 0.45 && prev <= 0.45) setProgressMessage('Roller filtreleniyor...');
        if (newProgress > 0.6 && prev <= 0.6) setProgressMessage('Kanıtlar tespit ediliyor...');
        if (newProgress > 0.8 && prev <= 0.8) setProgressMessage('Puanlar hesaplanıyor...');

        return newProgress;
      });
    }, 300);

    try {
      const response = await analyzeProfile({
        github_username: username,
        role_id: selectedRole,
        level: selectedLevel,
        github_token: githubToken || undefined,
        use_ai: false,
      });

      clearInterval(progressInterval);
      setProgress(1);
      setProgressMessage('Tamamlandı!');

      setTimeout(() => {
        setResult(response);
        setState('results');
      }, 600);
    } catch (err) {
      clearInterval(progressInterval);
      setError(err instanceof Error ? err.message : 'Analiz başarısız');
      setState('input');
    }
  };

  const handleReset = () => {
    setState('input');
    setResult(null);
    setProgress(0);
    setError('');
  };

  return (
    <main>
      {state === 'input' && (
        <div className="page-hero">
          <div className="hero-content animate-fade-in">
            <h1 className="hero-title">
              <span className="gradient-text">RoleGauge</span>
            </h1>
            <p className="hero-subtitle">
              GitHub profilinizi analiz edin, hedeflediğiniz role ne kadar hazır olduğunuzu öğrenin.
              AI destekli kanıt tespiti ve deterministik puanlama.
            </p>

            <div className={styles.formContainer}>
              <GitHubInput
                value={username}
                onChange={setUsername}
                token={githubToken}
                onTokenChange={setGithubToken}
              />

              {roles.length > 0 && (
                <RoleSelector
                  roles={roles}
                  selectedRole={selectedRole}
                  onRoleSelect={setSelectedRole}
                  selectedLevel={selectedLevel}
                  onLevelSelect={setSelectedLevel}
                />
              )}

              {error && (
                <div className={styles.errorBanner}>
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <circle cx="10" cy="10" r="9" stroke="currentColor" strokeWidth="1.5"/>
                    <path d="M10 6v5M10 13.5v.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
                  </svg>
                  {error}
                </div>
              )}

              <button
                className="btn btn-primary"
                onClick={handleAnalyze}
                disabled={!username.trim() || !selectedRole}
                style={{ width: '100%', padding: '16px', fontSize: '1.1rem', marginTop: '8px' }}
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
                </svg>
                Analizi Başlat
              </button>
            </div>
          </div>
        </div>
      )}

      {state === 'analyzing' && (
        <div className="page-hero">
          <AnalysisProgress
            progress={progress}
            message={progressMessage}
            username={username}
            role={selectedRole}
            level={selectedLevel}
          />
        </div>
      )}

      {state === 'results' && result && (
        <ResultsDashboard result={result} onReset={handleReset} />
      )}
    </main>
  );
}
