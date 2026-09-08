'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './MissingSkills.module.css';

interface MissingSkillsProps {
  t: (key: TranslationKey) => string;
}

export default function MissingSkills({ t }: MissingSkillsProps) {
  return (
    <section className={styles.section} id="missing-skills">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('missingSectionTag')}</span>
        <h2 className={styles.title}>{t('missingTitle')}</h2>
        <p className={styles.subtitle}>{t('missingSubtitle')}</p>
      </div>

      <div className={styles.cardsGrid}>
        {/* Evidenced Card */}
        <div className={styles.statusCard}>
          <div className={styles.cardTop}>
            <h3 className={styles.cardTitle}>{t('missingCardFoundTitle')}</h3>
            <span className={styles.badgeEvidenced}>
              ✓ {t('previewEvidencedBadge')}
            </span>
          </div>
          <p className={styles.cardDesc}>{t('missingCardFoundDesc')}</p>
        </div>

        {/* Not Yet Evidenced Card */}
        <div className={styles.statusCard}>
          <div className={styles.cardTop}>
            <h3 className={styles.cardTitle}>{t('missingCardNotYetTitle')}</h3>
            <span className={styles.badgeNotYet}>
              ○ {t('evidenceNotYet')}
            </span>
          </div>
          <p className={styles.cardDesc}>{t('missingCardNotYetDesc')}</p>
        </div>
      </div>

      {/* Interactive Verification Banner */}
      <div className={styles.interactiveBox}>
        <div className={styles.interactiveLeft}>
          <div className={styles.interactiveTitleRow}>
            <span className={styles.interactiveBadge}>
              {t('missingInteractiveBadge')}
            </span>
          </div>
          <p className={styles.interactiveDesc}>
            {t('missingInteractiveDesc')}
          </p>
        </div>
        <div className={styles.proveBtnPreview}>
          {t('evidenceProveSkill')} →
        </div>
      </div>
    </section>
  );
}
