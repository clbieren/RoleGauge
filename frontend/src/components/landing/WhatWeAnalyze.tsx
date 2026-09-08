'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './WhatWeAnalyze.module.css';

interface WhatWeAnalyzeProps {
  t: (key: TranslationKey) => string;
}

export default function WhatWeAnalyze({ t }: WhatWeAnalyzeProps) {
  const categories = [
    {
      title: t('analyzeCat1Title'),
      desc: t('analyzeCat1Desc'),
      items: [
        t('analyzeCat1Item1'),
        t('analyzeCat1Item2'),
        t('analyzeCat1Item3'),
      ],
    },
    {
      title: t('analyzeCat2Title'),
      desc: t('analyzeCat2Desc'),
      items: [
        t('analyzeCat2Item1'),
        t('analyzeCat2Item2'),
        t('analyzeCat2Item3'),
      ],
    },
    {
      title: t('analyzeCat3Title'),
      desc: t('analyzeCat3Desc'),
      items: [
        t('analyzeCat3Item1'),
        t('analyzeCat3Item2'),
        t('analyzeCat3Item3'),
      ],
    },
  ];

  return (
    <section className={styles.section} id="what-we-analyze">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('analyzeSectionTag')}</span>
        <h2 className={styles.title}>{t('analyzeTitle')}</h2>
        <p className={styles.subtitle}>{t('analyzeSubtitle')}</p>
      </div>

      <div className={styles.categoryGrid}>
        {categories.map((cat, idx) => (
          <div key={idx} className={styles.categoryCard}>
            <div className={styles.cardTop}>
              <h3 className={styles.categoryTitle}>{cat.title}</h3>
              <p className={styles.categoryDesc}>{cat.desc}</p>
            </div>
            <ul className={styles.itemList}>
              {cat.items.map((item, itemIdx) => (
                <li key={itemIdx} className={styles.item}>
                  <span className={styles.itemDot} />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
}
