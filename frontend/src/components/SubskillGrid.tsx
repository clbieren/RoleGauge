'use client';

import { useState } from 'react';
import { SkillScore, SubskillEvidence } from '@/lib/api';
import styles from './SubskillGrid.module.css';

interface SubskillGridProps {
  skills: SkillScore[];
}

export default function SubskillGrid({ skills }: SubskillGridProps) {
  const [expandedSkill, setExpandedSkill] = useState<string | null>(null);

  return (
    <div className={styles.container}>
      {skills.map((skill) => {
        const isExpanded = expandedSkill === skill.skill_id;
        const foundCount = skill.subskills.filter(s => s.status === 'evidence_found').length;
        const totalCount = skill.subskills.length;
        const scorePercent = Math.round(skill.score * 100);

        return (
          <div key={skill.skill_id} className={styles.skillCard}>
            <button
              className={styles.skillHeader}
              onClick={() => setExpandedSkill(isExpanded ? null : skill.skill_id)}
              type="button"
            >
              <div className={styles.skillInfo}>
                <span className={styles.skillName}>{skill.skill_name}</span>
                <span className={styles.skillMeta}>
                  {foundCount}/{totalCount} subskill kanıtlandı
                </span>
              </div>
              <div className={styles.skillRight}>
                <div className={styles.scoreBar}>
                  <div
                    className={styles.scoreBarFill}
                    style={{
                      width: `${scorePercent}%`,
                      background: scorePercent >= 70 ? 'var(--accent-emerald)' :
                                  scorePercent >= 40 ? 'var(--accent-amber)' :
                                  'var(--accent-rose)',
                    }}
                  />
                </div>
                <span className={`${styles.scoreValue} mono`}>{scorePercent}%</span>
                <svg
                  width="16" height="16" viewBox="0 0 24 24"
                  fill="none" stroke="currentColor" strokeWidth="2"
                  className={`${styles.chevron} ${isExpanded ? styles.chevronOpen : ''}`}
                >
                  <polyline points="6 9 12 15 18 9"/>
                </svg>
              </div>
            </button>

            {isExpanded && (
              <div className={styles.subskillList}>
                {skill.subskills.map((sub) => (
                  <SubskillRow key={sub.composite_key} subskill={sub} />
                ))}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}

function SubskillRow({ subskill }: { subskill: SubskillEvidence }) {
  const [showEvidence, setShowEvidence] = useState(false);
  const isFound = subskill.status === 'evidence_found';
  const confidence = Math.round(subskill.confidence * 100);

  return (
    <div className={styles.subskillRow}>
      <div className={styles.subskillMain}>
        <span className={`${styles.statusIcon} ${isFound ? styles.statusFound : styles.statusMissing}`}>
          {isFound ? '✓' : '—'}
        </span>
        <div className={styles.subskillInfo}>
          <span className={styles.subskillName}>{subskill.subskill_name}</span>
          <span className={`${styles.compositeKey} mono`}>{subskill.composite_key}</span>
        </div>
        <span className={`${styles.confidenceValue} mono ${isFound ? styles.confidenceFound : ''}`}>
          {confidence}%
        </span>
      </div>

      {isFound && subskill.evidence_sources.length > 0 && (
        <>
          <button
            className={styles.evidenceToggle}
            onClick={() => setShowEvidence(!showEvidence)}
            type="button"
          >
            {showEvidence ? 'Kanıtları gizle' : `${subskill.evidence_sources.length} kanıt göster`}
          </button>
          {showEvidence && (
            <div className={styles.evidenceList}>
              {subskill.evidence_sources.slice(0, 8).map((source, i) => (
                <div key={i} className={`${styles.evidenceItem} mono`}>
                  {source}
                </div>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}
