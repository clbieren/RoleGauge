'use client';

import { useState } from 'react';
import { RepoInfo } from '@/lib/api';
import { useLocale } from '@/lib/useLocale';
import styles from './RepoBreakdown.module.css';

interface RepoBreakdownProps {
  repos: RepoInfo[];
}

export default function RepoBreakdown({ repos }: RepoBreakdownProps) {
  const { t } = useLocale();
  const [openRepo, setOpenRepo] = useState<string | null>(null);

  // Sort: relevant first, then by stars
  const sorted = [...repos].sort((a, b) => {
    if (a.is_relevant !== b.is_relevant) return b.is_relevant ? 1 : -1;
    return b.stars - a.stars;
  });

  return (
    <div className={styles.container}>
      {/* Table header */}
      <div className={styles.tableHead}>
        <span className={styles.thCell}>{t('summaryRepositories')}</span>
        <span className={styles.thCell}>{t('repoStars')}</span>
        <span className={styles.thCell}>{t('repoLanguages')}</span>
        <span className={styles.thCell}>{t('repoRelevance')}</span>
      </div>

      {sorted.map(repo => {
        const isOpen = openRepo === repo.repo_name;
        const topLangs = Object.entries(repo.languages)
          .sort(([, a], [, b]) => b - a)
          .slice(0, 3)
          .map(([l]) => l)
          .join(' · ');

        return (
          <div key={repo.repo_name} className={styles.row}>
            {/* Row */}
            <div
              className={styles.rowMain}
              onClick={() => setOpenRepo(isOpen ? null : repo.repo_name)}
              role="button"
              tabIndex={0}
              onKeyDown={e => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault();
                  setOpenRepo(isOpen ? null : repo.repo_name);
                }
              }}
            >
              {/* Name */}
              <div className={styles.repoNameCell}>
                <svg
                  width="15" height="15" viewBox="0 0 16 16"
                  fill="currentColor" className={styles.repoIcon}
                >
                  <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z" />
                </svg>
                <span className={styles.repoName}>{repo.repo_name}</span>
                <svg
                  width="14" height="14" viewBox="0 0 24 24"
                  fill="none" stroke="currentColor" strokeWidth="2"
                  className={`${styles.chevron} ${isOpen ? styles.chevronOpen : ''}`}
                >
                  <polyline points="6 9 12 15 18 9" />
                </svg>
              </div>

              {/* Stars */}
              <span className={styles.stars}>
                <svg width="13" height="13" viewBox="0 0 16 16" fill="currentColor" className={styles.starIcon}>
                  <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z" />
                </svg>
                {repo.stars}
              </span>

              {/* Languages */}
              <span className={styles.langs}>{topLangs || '—'}</span>

              {/* Relevance */}
              <div className={styles.relevance}>
                <span className={`${styles.relevanceBadge} ${repo.is_relevant ? styles.relevantBadge : styles.irrelevantBadge}`}>
                  {repo.is_relevant ? t('repoRelevant') : t('repoNotRelevant')}
                </span>
              </div>
            </div>

            {/* Expanded detail */}
            {isOpen && (
              <div className={styles.detail}>
                {/* Description */}
                {repo.description && (
                  <div className={styles.detailSection}>
                    <p className={styles.detailDesc}>{repo.description}</p>
                  </div>
                )}

                {/* Evidence found */}
                {repo.is_relevant && repo.evidence_found.length > 0 && (
                  <div className={styles.detailSection}>
                    <p className={styles.detailLabel}>{t('repoEvidenceFound')}</p>
                    <div className={styles.evidenceList}>
                      {repo.evidence_found.map(ev => (
                        <div key={ev} className={styles.evidenceItem}>
                          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--success)" strokeWidth="2.5" className={styles.evidenceCheck}>
                            <polyline points="20 6 9 17 4 12" />
                          </svg>
                          <span>{ev.replace(/\./g, ' → ')}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Files */}
                {repo.relevant_files_count > 0 && (
                  <p className={styles.detailDesc} style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    {repo.relevant_files_count} {t('repoFiles')}
                  </p>
                )}

                {/* GitHub link */}
                <a
                  href={repo.repo_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={styles.githubLink}
                  onClick={e => e.stopPropagation()}
                >
                  {t('repoViewOnGitHub')}
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                    <polyline points="15 3 21 3 21 9"/>
                    <line x1="10" y1="14" x2="21" y2="3"/>
                  </svg>
                </a>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
