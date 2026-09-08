'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './FinalCTA.module.css';

interface FinalCTAProps {
  t: (key: TranslationKey) => string;
  onStartAnalysis: () => void;
  onViewSample: () => void;
}

export default function FinalCTA({
  t,
  onStartAnalysis,
  onViewSample,
}: FinalCTAProps) {
  return (
    <section className={styles.section}>
      <div className={styles.bannerCard}>
        <h2 className={styles.title}>{t('ctaTitle')}</h2>
        <p className={styles.subtitle}>{t('ctaSubtitle')}</p>

        <div className={styles.actionsRow}>
          <button
            type="button"
            className={`btn btn-primary ${styles.analyzeBtn}`}
            onClick={onStartAnalysis}
          >
            {t('ctaAnalyzeBtn')} ↑
          </button>
          <button
            type="button"
            className={styles.sampleBtn}
            onClick={onViewSample}
          >
            {t('ctaSampleBtn')} →
          </button>
        </div>
      </div>
    </section>
  );
}
