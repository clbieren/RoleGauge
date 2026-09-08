'use client';

import React from 'react';
import { Locale, TranslationKey } from '@/lib/i18n';
import styles from './LandingNav.module.css';

interface LandingNavProps {
  locale: Locale;
  toggleLocale: () => void;
  t: (key: TranslationKey) => string;
  onLogoClick?: () => void;
}

export default function LandingNav({ locale, toggleLocale, t, onLogoClick }: LandingNavProps) {
  const scrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <nav className={styles.nav}>
      <div className={styles.navInner}>
        <button className={styles.logo} onClick={onLogoClick} aria-label="SkillLens Home">
          <span className={styles.logoMark}>◈</span>
          SkillLens
        </button>

        <div className={styles.navLinks}>
          <button className={styles.navLink} onClick={() => scrollTo('how-it-works')}>
            {t('navHowItWorks')}
          </button>
          <button className={styles.navLink} onClick={() => scrollTo('what-we-analyze')}>
            {t('navWhatWeAnalyze')}
          </button>
          <button className={styles.navLink} onClick={() => scrollTo('code-evidence')}>
            {t('navEvidence')}
          </button>
          <button className={styles.navLink} onClick={() => scrollTo('sample-analysis')}>
            {t('navSampleAnalysis')}
          </button>
          <button className={styles.navLink} onClick={() => scrollTo('trust-security')}>
            {t('navTrust')}
          </button>
        </div>

        <div className={styles.navRight}>
          <button className={styles.signInBtn} type="button">
            {t('navSignIn')}
          </button>

          <div className={styles.localePill} role="group" aria-label="Language selector">
            <button
              type="button"
              className={`${styles.localeBtn} ${locale === 'tr' ? styles.localeBtnActive : ''}`}
              onClick={() => locale !== 'tr' && toggleLocale()}
              aria-label="Türkçe"
            >
              TR
            </button>
            <button
              type="button"
              className={`${styles.localeBtn} ${locale === 'en' ? styles.localeBtnActive : ''}`}
              onClick={() => locale !== 'en' && toggleLocale()}
              aria-label="English"
            >
              EN
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}
