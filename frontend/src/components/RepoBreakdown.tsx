'use client';

import { RepoInfo } from '@/lib/api';
import styles from './RepoBreakdown.module.css';

interface RepoBreakdownProps {
  repos: RepoInfo[];
}

const LANG_COLORS: Record<string, string> = {
  'C#': '#178600',
  'C++': '#f34b7d',
  'Python': '#3572A5',
  'JavaScript': '#f1e05a',
  'TypeScript': '#3178c6',
  'Java': '#b07219',
  'Go': '#00ADD8',
  'Rust': '#dea584',
  'Ruby': '#701516',
  'GDScript': '#355570',
  'ShaderLab': '#222c37',
  'HLSL': '#aace60',
  'GLSL': '#5686a5',
  'Swift': '#F05138',
  'Kotlin': '#A97BFF',
  'Dart': '#00B4AB',
};

export default function RepoBreakdown({ repos }: RepoBreakdownProps) {
  // Sort: relevant first, then by stars
  const sorted = [...repos].sort((a, b) => {
    if (a.is_relevant !== b.is_relevant) return b.is_relevant ? 1 : -1;
    return b.stars - a.stars;
  });

  return (
    <div className={styles.container}>
      {sorted.map((repo) => {
        const totalBytes = Object.values(repo.languages).reduce((a, b) => a + b, 0);

        return (
          <a
            key={repo.repo_name}
            href={repo.repo_url}
            target="_blank"
            rel="noopener noreferrer"
            className={`${styles.repoCard} ${repo.is_relevant ? styles.relevant : styles.irrelevant}`}
          >
            <div className={styles.repoHeader}>
              <div className={styles.repoTitle}>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style={{ flexShrink: 0 }}>
                  <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z" />
                </svg>
                <span className={styles.repoName}>{repo.repo_name}</span>
                {repo.is_relevant && (
                  <span className={styles.relevantBadge}>İlgili</span>
                )}
              </div>
              <div className={styles.repoStats}>
                {repo.stars > 0 && (
                  <span className={styles.stat}>
                    <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor">
                      <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z" />
                    </svg>
                    {repo.stars}
                  </span>
                )}
                {repo.relevant_files_count > 0 && (
                  <span className={styles.stat}>
                    {repo.relevant_files_count} dosya
                  </span>
                )}
              </div>
            </div>

            {repo.description && (
              <p className={styles.repoDesc}>{repo.description}</p>
            )}

            {totalBytes > 0 && (
              <div className={styles.langBar}>
                {Object.entries(repo.languages)
                  .sort(([, a], [, b]) => b - a)
                  .map(([lang, bytes]) => (
                    <div
                      key={lang}
                      className={styles.langSegment}
                      style={{
                        width: `${(bytes / totalBytes) * 100}%`,
                        backgroundColor: LANG_COLORS[lang] || '#8b8b8b',
                      }}
                      title={`${lang}: ${Math.round((bytes / totalBytes) * 100)}%`}
                    />
                  ))}
              </div>
            )}

            {Object.keys(repo.languages).length > 0 && (
              <div className={styles.langList}>
                {Object.entries(repo.languages)
                  .sort(([, a], [, b]) => b - a)
                  .slice(0, 5)
                  .map(([lang, bytes]) => (
                    <span key={lang} className={styles.langTag}>
                      <span
                        className={styles.langDot}
                        style={{ backgroundColor: LANG_COLORS[lang] || '#8b8b8b' }}
                      />
                      {lang}
                      <span className={styles.langPercent}>
                        {Math.round((bytes / totalBytes) * 100)}%
                      </span>
                    </span>
                  ))}
              </div>
            )}
          </a>
        );
      })}
    </div>
  );
}
