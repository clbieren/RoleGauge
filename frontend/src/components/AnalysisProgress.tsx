'use client';

import { Locale, tLevelLabel } from '@/lib/i18n';
import AdPlacement from './AdPlacement';
import styles from './AnalysisProgress.module.css';

interface AnalysisProgressProps {
  currentStep: number;   // 0-5 (0 = not started, 5 = done)
  steps: string[];       // 5 step labels (localized)
  username: string;
  roleName: string;
  level: string;
  locale: string;
}

export default function AnalysisProgress({
  currentStep,
  steps,
  username,
  roleName,
  level,
  locale,
}: AnalysisProgressProps) {
  const progressPct = Math.min(Math.round((currentStep / steps.length) * 100), 95);
  const loc = (locale === 'en' ? 'en' : 'tr') as Locale;

  return (
    <div className={styles.page}>
      <div className={styles.card}>
        <p className={styles.title}>
          {roleName || (loc === 'tr' ? 'Profil' : 'Profile')} · {tLevelLabel(level, loc)}
        </p>
        <p className={styles.subtitle}>@{username}</p>

        {/* Thin progress bar */}
        <div className={styles.track}>
          <div className={styles.fill} style={{ width: `${progressPct}%` }} />
        </div>

        {/* Step list */}
        <div className={styles.steps}>
          {steps.map((label, i) => {
            const isDone   = i < currentStep;
            const isActive = i === currentStep;

            return (
              <div key={i} className={styles.step}>
                {/* Icon */}
                <span className={styles.stepIcon}>
                  {isDone ? (
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--success)" strokeWidth="2.5">
                      <polyline points="20 6 9 17 4 12"/>
                    </svg>
                  ) : isActive ? (
                    <span className="spinner" />
                  ) : (
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" strokeWidth="2">
                      <circle cx="12" cy="12" r="9"/>
                    </svg>
                  )}
                </span>

                {/* Label */}
                <span
                  className={
                    isDone
                      ? styles.stepLabelDone
                      : isActive
                      ? styles.stepLabelActive
                      : styles.stepLabelPending
                  }
                >
                  {label}
                </span>
              </div>
            );
          })}
        </div>
      </div>

      <AdPlacement slot="loading_screen" enabled={true} locale={locale} />
    </div>
  );
}
