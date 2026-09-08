'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './PersonasSection.module.css';

interface PersonasSectionProps {
  t: (key: TranslationKey) => string;
}

export default function PersonasSection({ t }: PersonasSectionProps) {
  const personas = [
    {
      tag: 'ENTRY_LEVEL',
      title: t('persona1Title'),
      desc: t('persona1Desc'),
    },
    {
      tag: 'CAREER_GROWTH',
      title: t('persona2Title'),
      desc: t('persona2Desc'),
    },
    {
      tag: 'PORTFOLIO_PROOF',
      title: t('persona3Title'),
      desc: t('persona3Desc'),
    },
  ];

  return (
    <section className={styles.section} id="personas">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('personasSectionTag')}</span>
        <h2 className={styles.title}>{t('personasTitle')}</h2>
        <p className={styles.subtitle}>{t('personasSubtitle')}</p>
      </div>

      <div className={styles.personaGrid}>
        {personas.map((persona, idx) => (
          <div key={idx} className={styles.personaCard}>
            <span className={styles.personaTag}>{persona.tag}</span>
            <h3 className={styles.personaTitle}>{persona.title}</h3>
            <p className={styles.personaDesc}>{persona.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
