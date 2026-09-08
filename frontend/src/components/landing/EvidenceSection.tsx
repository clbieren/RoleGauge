'use client';

import React from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './EvidenceSection.module.css';

interface EvidenceSectionProps {
  t: (key: TranslationKey) => string;
}

export default function EvidenceSection({ t }: EvidenceSectionProps) {
  const snippets = [
    {
      file: t('evidenceSnippetFile1'),
      desc: t('evidenceSnippetDesc1'),
    },
    {
      file: t('evidenceSnippetFile2'),
      desc: t('evidenceSnippetDesc2'),
    },
    {
      file: t('evidenceSnippetFile3'),
      desc: t('evidenceSnippetDesc3'),
    },
  ];

  return (
    <section className={styles.section} id="code-evidence">
      <div className={styles.header}>
        <span className={styles.sectionTag}>{t('evidenceSectionTag')}</span>
        <h2 className={styles.title}>{t('evidenceTitle')}</h2>
        <p className={styles.subtitle}>{t('evidenceSubtitle')}</p>
      </div>

      <div className={styles.snippetContainer}>
        <div className={styles.snippetHeader}>
          <div className={styles.terminalDots}>
            <span className={styles.dot} />
            <span className={styles.dot} />
            <span className={styles.dot} />
          </div>
          <span className={styles.snippetTitle}>evidence_provenance_ast.log</span>
        </div>

        <div className={styles.snippetList}>
          {snippets.map((snip, idx) => (
            <div key={idx} className={styles.snippetItem}>
              <div className={styles.itemLeft}>
                <span className={styles.filePath}>{snip.file}</span>
                <span className={styles.signalDesc}>{snip.desc}</span>
              </div>
              <span className={styles.verifiedBadge}>
                ✓ {t('evidenceStatusVerified')}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
