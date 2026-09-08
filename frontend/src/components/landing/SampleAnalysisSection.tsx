'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './SampleAnalysisSection.module.css';

interface SampleAnalysisSectionProps {
  t: (key: TranslationKey) => string;
  onViewSample: () => void;
}

export default function SampleAnalysisSection({
  t,
  onViewSample,
}: SampleAnalysisSectionProps) {
  return (
    <section className={styles.section} id="sample-analysis">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('sampleSectionTag')}</span>
        <h2 className={styles.title}>{t('sampleTitle')}</h2>
        <p className={styles.subtitle}>{t('sampleSubtitle')}</p>
      </div>

      <div className={styles.card}>
        <div className={styles.cardLeft}>
          <div className={styles.avatar}>
            <span>DD</span>
          </div>

          <div className={styles.infoCol}>
            <div className={styles.userTitleRow}>
              <span className={styles.username}>{t('sampleProfileUser')}</span>
              <span className={styles.demoPill}>{t('sampleSyntheticTag')}</span>
            </div>
            <span className={styles.roleMeta}>{t('sampleProfileRole')}</span>
            <div className={styles.statsRow}>
              <span className={styles.statItem}>{t('sampleRepos')}</span>
              <span className={styles.statItem}>·</span>
              <span className={styles.statItem}>Python / FastAPI / PostgreSQL</span>
            </div>
          </div>
        </div>

        <div className={styles.cardRight}>
          <div className={styles.readinessBox}>
            <span className={styles.scoreVal}>{t('sampleReadiness')}</span>
            <span className={styles.scoreLabel}>{t('dashboardReadiness')}</span>
          </div>

          <button
            type="button"
            className={`btn btn-primary ${styles.viewBtn}`}
            onClick={onViewSample}
          >
            {t('sampleActionBtn')} →
          </button>
        </div>
      </div>
    </section>
  );
}
