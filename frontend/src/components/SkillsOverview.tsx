'use client';

import styles from './SkillsOverview.module.css';
import { SkillScore } from '@/lib/api';
import { tSkillName } from '@/lib/skillTranslations';
import { useLocale } from '@/lib/useLocale';

interface SkillsOverviewProps {
  skills: SkillScore[];
}

function barColor(score: number): string {
  if (score >= 0.7) return 'var(--success)';
  if (score >= 0.4) return 'var(--warning)';
  return 'var(--text-muted)';
}

export default function SkillsOverview({ skills }: SkillsOverviewProps) {
  const { locale } = useLocale();
  // Sort by score descending
  const sorted = [...skills].sort((a, b) => b.score - a.score);

  return (
    <div className={styles.container}>
      {sorted.map(skill => {
        const pct = Math.round(skill.score * 100);
        const displayName = tSkillName(skill.skill_name, locale);
        return (
          <div key={skill.skill_id} className={styles.row}>
            <span className={styles.name} title={displayName}>
              {displayName}
            </span>
            <div className={styles.barWrap}>
              <div
                className={styles.barFill}
                style={{ width: `${pct}%`, background: barColor(skill.score) }}
              />
            </div>
            <span className={styles.score}>{pct}%</span>
          </div>
        );
      })}
    </div>
  );
}
