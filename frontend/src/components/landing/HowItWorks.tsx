'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './HowItWorks.module.css';

interface HowItWorksProps {
  t: (key: TranslationKey) => string;
}

export default function HowItWorks({ t }: HowItWorksProps) {
  const steps = [
    {
      num: t('step1Number'),
      title: t('step1Title'),
      desc: t('step1Desc'),
    },
    {
      num: t('step2Number'),
      title: t('step2Title'),
      desc: t('step2Desc'),
    },
    {
      num: t('step3Number'),
      title: t('step3Title'),
      desc: t('step3Desc'),
    },
  ];

  return (
    <section className={styles.section} id="how-it-works">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('howSectionTag')}</span>
        <h2 className={styles.title}>{t('howTitle')}</h2>
        <p className={styles.subtitle}>{t('howSubtitle')}</p>
      </div>

      <div className={styles.stepsGrid}>
        {steps.map(step => (
          <div key={step.num} className={styles.stepCard}>
            <span className={styles.stepNum}>{step.num}</span>
            <h3 className={styles.stepTitle}>{step.title}</h3>
            <p className={styles.stepDesc}>{step.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
