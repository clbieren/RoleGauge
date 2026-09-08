'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './TrustSection.module.css';

interface TrustSectionProps {
  t: (key: TranslationKey) => string;
}

export default function TrustSection({ t }: TrustSectionProps) {
  const pillars = [
    {
      title: t('trustPillar1Title'),
      desc: t('trustPillar1Desc'),
      icon: (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="12" cy="12" r="10" />
          <path d="M2 12h20" />
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
        </svg>
      ),
    },
    {
      title: t('trustPillar2Title'),
      desc: t('trustPillar2Desc'),
      icon: (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
          <path d="M7 11V7a5 5 0 0 1 10 0v4" />
        </svg>
      ),
    },
    {
      title: t('trustPillar3Title'),
      desc: t('trustPillar3Desc'),
      icon: (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M21 2l-2 2m-1-1l2 2" />
          <path d="M15.5 8.5l3 3L7 23l-4-1 1-4L15.5 8.5z" />
        </svg>
      ),
    },
    {
      title: t('trustPillar4Title'),
      desc: t('trustPillar4Desc'),
      icon: (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
        </svg>
      ),
    },
  ];

  return (
    <section className={styles.section} id="trust-security">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('trustSectionTag')}</span>
        <h2 className={styles.title}>{t('trustTitle')}</h2>
        <p className={styles.subtitle}>{t('trustSubtitle')}</p>
      </div>

      <div className={styles.trustGrid}>
        {pillars.map((item, idx) => (
          <div key={idx} className={styles.trustCard}>
            <div className={styles.trustIconWrap}>{item.icon}</div>
            <h3 className={styles.trustTitle}>{item.title}</h3>
            <p className={styles.trustDesc}>{item.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
