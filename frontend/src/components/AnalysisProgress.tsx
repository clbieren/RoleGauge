'use client';

import styles from './AnalysisProgress.module.css';

interface AnalysisProgressProps {
  progress: number;
  message: string;
  username: string;
  role: string;
  level: string;
}

export default function AnalysisProgress({ progress, message, username, role, level }: AnalysisProgressProps) {
  const percentage = Math.round(progress * 100);

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <div className={styles.header}>
          <div className={styles.avatar}>
            <img
              src={`https://github.com/${username}.png?size=80`}
              alt={username}
              className={styles.avatarImg}
              onError={(e) => {
                (e.target as HTMLImageElement).style.display = 'none';
              }}
            />
          </div>
          <div>
            <h2 className={styles.username}>@{username}</h2>
            <p className={styles.meta}>
              {role.replace('-', ' ')} · {level}
            </p>
          </div>
        </div>

        <div className={styles.progressTrack}>
          <div
            className={styles.progressFill}
            style={{ width: `${percentage}%` }}
          />
        </div>

        <div className={styles.info}>
          <span className={styles.message}>
            <span className={styles.spinner} />
            {message}
          </span>
          <span className={`${styles.percentage} mono`}>{percentage}%</span>
        </div>

        <div className={styles.steps}>
          {['Repo Tarama', 'Filtreleme', 'Kanıt Tespiti', 'Puanlama'].map((step, i) => {
            const stepProgress = (i + 1) / 4;
            const isActive = progress >= stepProgress - 0.25 && progress < stepProgress;
            const isDone = progress >= stepProgress;
            return (
              <div
                key={step}
                className={`${styles.step} ${isDone ? styles.stepDone : ''} ${isActive ? styles.stepActive : ''}`}
              >
                <div className={styles.stepDot}>
                  {isDone ? '✓' : i + 1}
                </div>
                <span className={styles.stepLabel}>{step}</span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
