'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './LandingFooter.module.css';

interface LandingFooterProps {
  t: (key: TranslationKey) => string;
}

export default function LandingFooter({ t }: LandingFooterProps) {
  const scrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <footer className={styles.footer}>
      <div className={styles.inner}>
        <div className={styles.topRow}>
          <div className={styles.brandCol}>
            <div className={styles.logo}>
              <span className={styles.logoMark}>◈</span>
              SkillLens
            </div>
            <p className={styles.tagline}>{t('footerTagline')}</p>
          </div>

          <div className={styles.linksRow}>
            <button
              type="button"
              className={styles.footerLink}
              onClick={() => scrollTo('how-it-works')}
            >
              {t('navHowItWorks')}
            </button>
            <button
              type="button"
              className={styles.footerLink}
              onClick={() => scrollTo('what-we-analyze')}
            >
              {t('navWhatWeAnalyze')}
            </button>
            <button
              type="button"
              className={styles.footerLink}
              onClick={() => scrollTo('code-evidence')}
            >
              {t('navEvidence')}
            </button>
            <button
              type="button"
              className={styles.footerLink}
              onClick={() => scrollTo('sample-analysis')}
            >
              {t('navSampleAnalysis')}
            </button>
            <button
              type="button"
              className={styles.footerLink}
              onClick={() => scrollTo('trust-security')}
            >
              {t('navTrust')}
            </button>
          </div>
        </div>

        <div className={styles.bottomRow}>
          <p className={styles.privacyNote}>{t('footerPrivacyNote')}</p>
          <p>© {new Date().getFullYear()} SkillLens. {t('footerRights')}</p>
        </div>
      </div>
    </footer>
  );
}
