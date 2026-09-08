'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './RoleComparison.module.css';

interface RoleComparisonProps {
  t: (key: TranslationKey) => string;
}

export default function RoleComparison({ t }: RoleComparisonProps) {
  const comparisons = [
    {
      role: t('compareRole1'),
      score: t('compareRole1Score'),
      numeric: 91,
      tier: t('compareRole1Tier'),
      tierClass: styles.tierReady,
      barColor: 'var(--success)',
    },
    {
      role: t('compareRole2'),
      score: t('compareRole2Score'),
      numeric: 64,
      tier: t('compareRole2Tier'),
      tierClass: styles.tierDeveloping,
      barColor: 'var(--warning)',
    },
    {
      role: t('compareRole3'),
      score: t('compareRole3Score'),
      numeric: 42,
      tier: t('compareRole3Tier'),
      tierClass: styles.tierNotReady,
      barColor: 'var(--text-muted)',
    },
  ];

  return (
    <section className={styles.section} id="role-comparison">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('compareSectionTag')}</span>
        <h2 className={styles.title}>{t('compareTitle')}</h2>
        <p className={styles.subtitle}>{t('compareSubtitle')}</p>
      </div>

      <div className={styles.comparisonGrid}>
        {comparisons.map((item, idx) => (
          <div key={idx} className={styles.compareCard}>
            <div className={styles.cardTop}>
              <h3 className={styles.roleTitle}>{item.role}</h3>
              <span className={`${styles.tierBadge} ${item.tierClass}`}>
                {item.tier}
              </span>
            </div>

            <div className={styles.scoreRow}>
              <span className={styles.scoreVal}>{item.score}</span>
            </div>

            <div className={styles.barTrack}>
              <div
                className={styles.barFill}
                style={{
                  width: `${item.numeric}%`,
                  backgroundColor: item.barColor,
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
