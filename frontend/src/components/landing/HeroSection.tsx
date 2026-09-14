'use client';

import React, { useRef, useState } from 'react';
import { RoleInfo } from '@/lib/api';
import { Locale, TranslationKey } from '@/lib/i18n';
import DashboardPreview from './DashboardPreview';
import styles from './HeroSection.module.css';

interface HeroSectionProps {
  username: string;
  setUsername: (val: string) => void;
  selectedRole: string;
  setSelectedRole: (val: string) => void;
  selectedLevel: 'junior' | 'mid' | 'senior';
  setSelectedLevel: (val: 'junior' | 'mid' | 'senior') => void;
  githubToken: string;
  setGithubToken: (val: string) => void;
  showToken: boolean;
  setShowToken: React.Dispatch<React.SetStateAction<boolean>>;
  uploadedFile?: File | null;
  setUploadedFile?: (file: File | null) => void;
  roles: RoleInfo[];
  error: string;
  onAnalyze: () => void;
  onViewSample: () => void;
  t: (key: TranslationKey) => string;
  locale: Locale;
}

const LEVEL_KEYS = ['junior', 'mid', 'senior'] as const;

export default function HeroSection({
  username,
  setUsername,
  selectedRole,
  setSelectedRole,
  selectedLevel,
  setSelectedLevel,
  githubToken,
  setGithubToken,
  showToken,
  setShowToken,
  uploadedFile,
  setUploadedFile,
  roles,
  error,
  onAnalyze,
  onViewSample,
  t,
  locale,
}: HeroSectionProps) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isDragging, setIsDragging] = useState(false);

  const formatSize = (bytes: number) => {
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && setUploadedFile) {
      setUploadedFile(file);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const file = e.dataTransfer.files?.[0];
    if (file && setUploadedFile) {
      setUploadedFile(file);
    }
  };

  const handleRemoveFile = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (setUploadedFile) setUploadedFile(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };
  return (
    <section className={styles.hero} id="hero-section">
      {/* Top Header: Badge, Title, Subtitle */}
      <div className={styles.heroHeader}>
        <div className={styles.badge}>
          <span className={styles.badgeDot} />
          <span>{t('heroBadge')}</span>
        </div>

        <h1 className={styles.title}>{t('heroTitle')}</h1>
        <p className={styles.subtitle}>{t('heroSubtitle')}</p>
      </div>

      {/* Balanced 2-Column Grid: Form Left, Multi-Demo Showcase Right */}
      <div className={styles.heroGrid}>
        {/* Left Column: Analysis Form Card */}
        <div className={styles.leftCol}>
          <div className={styles.formCard}>
            {/* GitHub Username */}
            <div className={styles.formField}>
              <label className={styles.formLabel} htmlFor="hero-github-input">
                {t('formGithubLabel')}
              </label>
              <div className={styles.githubInputWrap}>
                <span className={styles.githubPrefix}>github.com/</span>
                <input
                  id="hero-github-input"
                  type="text"
                  className={styles.githubInput}
                  placeholder={t('formGithubPlaceholder')}
                  value={username}
                  onChange={e => setUsername(e.target.value)}
                  autoComplete="off"
                  spellCheck={false}
                  onKeyDown={e => {
                    if (e.key === 'Enter' && username.trim() && selectedRole) {
                      onAnalyze();
                    }
                  }}
                />
              </div>
            </div>

            {/* Target Role */}
            <div className={styles.formField}>
              <label className={styles.formLabel} htmlFor="hero-role-select">
                {t('formRoleLabel')}
              </label>
              <select
                id="hero-role-select"
                className="select"
                value={selectedRole}
                onChange={e => setSelectedRole(e.target.value)}
              >
                <option value="">{t('formRolePlaceholder')}</option>
                {roles.map(r => (
                  <option key={r.role_id} value={r.role_id}>
                    {r.title.replace(/^(Junior|Mid|Senior)\s+/i, '')}
                  </option>
                ))}
              </select>
            </div>

            {/* Level selector */}
            <div className={styles.formField}>
              <label className={styles.formLabel}>{t('formLevelLabel')}</label>
              <div className={styles.levelGroup}>
                {LEVEL_KEYS.map(lv => {
                  const levelLabels: Record<string, string> = {
                    junior: t('formLevelJunior'),
                    mid: t('formLevelMid'),
                    senior: t('formLevelSenior'),
                  };
                  return (
                    <button
                      key={lv}
                      type="button"
                      className={`${styles.levelBtn} ${
                        selectedLevel === lv ? styles.levelBtnActive : ''
                      }`}
                      onClick={() => setSelectedLevel(lv)}
                    >
                      {levelLabels[lv]}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* CV / LinkedIn upload dropzone */}
            <div className={styles.formField}>
              <input
                ref={fileInputRef}
                type="file"
                accept=".pdf,.docx"
                style={{ display: 'none' }}
                onChange={handleFileChange}
              />

              {uploadedFile ? (
                <div className={styles.fileChip}>
                  <div className={styles.fileChipLeft}>
                    <span className={styles.fileIcon}>📄</span>
                    <div className={styles.fileMeta}>
                      <span className={styles.fileName} title={uploadedFile.name}>
                        {uploadedFile.name}
                      </span>
                      <span className={styles.fileSize}>{formatSize(uploadedFile.size)}</span>
                    </div>
                  </div>
                  <button
                    type="button"
                    className={styles.fileRemoveBtn}
                    onClick={handleRemoveFile}
                    title={locale === 'tr' ? 'Dosyayı kaldır' : 'Remove file'}
                  >
                    ✕
                  </button>
                </div>
              ) : (
                <div
                  className={`${styles.uploadDropzone} ${isDragging ? styles.uploadDropzoneDragOver : ''}`}
                  onClick={() => fileInputRef.current?.click()}
                  onDragOver={handleDragOver}
                  onDragLeave={handleDragLeave}
                  onDrop={handleDrop}
                >
                  <span className={styles.uploadBadge}>PDF / DOCX</span>
                  <div className={styles.uploadIcon}>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                      <polyline points="17 8 12 3 7 8" />
                      <line x1="12" y1="3" x2="12" y2="15" />
                    </svg>
                  </div>
                  <p className={styles.uploadTitle}>
                    {locale === 'tr' ? 'CV veya LinkedIn Profili Yükle' : 'Upload CV or LinkedIn Profile'}
                  </p>
                  <p className={styles.uploadDesc}>
                    {locale === 'tr' ? 'Dosya seçin veya buraya sürükleyin' : 'Choose a file or drag & drop here'}
                  </p>
                </div>
              )}
            </div>

            {/* Optional GitHub Token Accordion */}
            <div className={styles.formField}>
              <button
                type="button"
                className={styles.tokenToggle}
                onClick={() => setShowToken(v => !v)}
              >
                <svg
                  width="13"
                  height="13"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                >
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
                {t('formTokenToggle')}
                <svg
                  width="11"
                  height="11"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  style={{
                    transform: showToken ? 'rotate(180deg)' : 'none',
                    transition: 'transform 0.15s',
                  }}
                >
                  <polyline points="6 9 12 15 18 9" />
                </svg>
              </button>
              {showToken && (
                <div style={{ marginTop: 6 }}>
                  <input
                    type="password"
                    className="input"
                    placeholder="ghp_xxxxxxxxxxxxxxxxxxxx"
                    value={githubToken}
                    onChange={e => setGithubToken(e.target.value)}
                    autoComplete="off"
                  />
                  <p className={styles.tokenHint}>
                    {t('formTokenHint')}
                  </p>
                </div>
              )}
            </div>

            {/* Error Message */}
            {error && (
              <div className={styles.error}>
                <svg
                  width="15"
                  height="15"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  style={{ flexShrink: 0, marginTop: 1 }}
                >
                  <circle cx="12" cy="12" r="10" />
                  <line x1="12" y1="8" x2="12" y2="12" />
                  <line x1="12" y1="8" x2="12.01" y2="16" />
                </svg>
                <span>{error}</span>
              </div>
            )}

            {/* Submit Button */}
            <button
              type="button"
              className={`btn btn-primary ${styles.analyzeBtn}`}
              onClick={onAnalyze}
              disabled={(!username.trim() && !uploadedFile) || !selectedRole}
            >
              {uploadedFile && !username.trim()
                ? (locale === 'tr' ? 'CV ve Profili Analiz Et' : 'Analyze CV & Profile')
                : t('formAnalyzeBtn')}
            </button>

            {/* Quick Demo Analysis Link */}
            <div className={styles.quickSampleLink}>
              <button
                type="button"
                className={styles.quickSampleBtn}
                onClick={onViewSample}
              >
                {t('heroQuickSample')} →
              </button>
            </div>
          </div>
        </div>

        {/* Right Column: Multi-Profile Demo Showcase */}
        <div className={styles.rightCol}>
          <DashboardPreview t={t} onExploreClick={onViewSample} />
        </div>
      </div>
    </section>
  );
}
