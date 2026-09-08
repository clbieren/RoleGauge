'use client';

import { useState } from 'react';
import { SkillScore, SubskillEvidence } from '@/lib/api';
import { tSkillName, tSubskillName } from '@/lib/skillTranslations';
import { useLocale } from '@/lib/useLocale';
import { TranslationKey } from '@/lib/i18n';
import styles from './SubskillGrid.module.css';

interface SubskillGridProps {
  skills: SkillScore[];
  onProveSkill?: (compositeKey: string, subskillName: string) => void;
}

export default function SubskillGrid({ skills, onProveSkill }: SubskillGridProps) {
  const { locale, t } = useLocale();
  const [openSkill, setOpenSkill] = useState<string | null>(
    skills.length > 0 ? skills[0].skill_id : null
  );

  return (
    <div className={styles.container}>
      {skills.map(skill => {
        const isOpen = openSkill === skill.skill_id;
        const pct = Math.round(skill.score * 100);
        const evidencedCount = skill.subskills.filter(
          s => s.status === 'evidence_found'
        ).length;
        const skillDisplayName = tSkillName(skill.skill_name, locale);

        return (
          <div key={skill.skill_id} className={styles.skillRow}>
            <button
              type="button"
              className={styles.skillHeader}
              onClick={() => setOpenSkill(isOpen ? null : skill.skill_id)}
              aria-expanded={isOpen}
            >
              <div className={styles.skillLeft}>
                <span className={styles.skillName}>{skillDisplayName}</span>
                <span className={styles.skillMeta}>
                  {evidencedCount}/{skill.subskills.length} {t('skillsEvidenced')}
                </span>
              </div>
              <div className={styles.skillRight}>
                <span className={styles.skillScore}>{pct}%</span>
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  className={`${styles.chevron} ${isOpen ? styles.chevronOpen : ''}`}
                >
                  <polyline points="6 9 12 15 18 9" />
                </svg>
              </div>
            </button>

            {isOpen && (
              <div className={styles.subskillList}>
                {skill.subskills.map(sub => (
                  <SubskillRow
                    key={sub.composite_key}
                    sub={sub}
                    locale={locale}
                    t={t}
                    onProveSkill={onProveSkill}
                  />
                ))}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}

function SubskillRow({
  sub,
  locale,
  t,
  onProveSkill,
}: {
  sub: SubskillEvidence;
  locale: string;
  t: (key: TranslationKey) => string;
  onProveSkill?: (compositeKey: string, subskillName: string) => void;
}) {
  const isFound   = sub.status === 'evidence_found';
  const isClaimed = sub.status === 'claimed';
  // anything else → not yet evidenced
  const isNotYet  = !isFound && !isClaimed;

  const pct = Math.round(sub.confidence * 100);
  const MAX_SOURCES = 6;
  const subskillDisplayName = tSubskillName(sub.subskill_name, locale);

  return (
    <div className={styles.subskill}>
      <div className={styles.subskillMain}>
        <div className={styles.subskillNameWrap}>
          <span className={styles.subskillName}>{subskillDisplayName}</span>

          {/* Status line */}
          <div className={styles.statusLine}>
            {isFound && (
              <>
                <svg
                  width="13" height="13" viewBox="0 0 24 24"
                  fill="none" stroke="var(--success)" strokeWidth="2.5"
                  className={styles.statusIcon}
                >
                  <polyline points="20 6 9 17 4 12" />
                </svg>
                <span className={styles.statusFound}>{t('evidenceFound')}</span>
              </>
            )}
            {isClaimed && (
              <>
                <svg
                  width="13" height="13" viewBox="0 0 24 24"
                  fill="none" stroke="var(--info)" strokeWidth="2"
                  className={styles.statusIcon}
                >
                  <circle cx="12" cy="12" r="10" />
                  <line x1="12" y1="8" x2="12" y2="12" />
                  <line x1="12" y1="16" x2="12.01" y2="16" />
                </svg>
                <span className={styles.statusClaimed}>{t('evidenceClaimed')}</span>
              </>
            )}
            {isNotYet && (
              <>
                <span className={styles.statusNotYet} style={{ fontSize: '1rem', lineHeight: 1 }}>—</span>
                <span className={styles.statusNotYet}>{t('evidenceNotYet')}</span>
              </>
            )}
          </div>

          {/* Extra description for claimed / not-yet */}
          {isClaimed && (
            <p className={styles.statusDesc}>{t('evidenceClaimedDesc')}</p>
          )}
          {isNotYet && (
            <p className={styles.statusDesc}>{t('evidenceNotYetDesc')}</p>
          )}
        </div>

        {/* Score */}
        <span className={styles.subskillScore}>{pct}%</span>
      </div>

      {/* Evidence sources (only for found) */}
      {isFound && sub.evidence_sources.length > 0 && (
        <div className={styles.evidenceSources}>
          <p className={styles.evidenceLabel}>{t('evidenceSources')}</p>
          {sub.evidence_sources.slice(0, MAX_SOURCES).map((src, i) => (
            <span key={i} className={styles.evidenceSource}>
              {src}
            </span>
          ))}
          {sub.evidence_sources.length > MAX_SOURCES && (
            <span className={styles.evidenceMore}>
              +{sub.evidence_sources.length - MAX_SOURCES} {t('evidenceMore')}
            </span>
          )}
        </div>
      )}

      {/* Prove skill CTA for not-yet-evidenced */}
      {isNotYet && (
        <button
          type="button"
          className={styles.proveBtn}
          onClick={() => onProveSkill?.(sub.composite_key, sub.subskill_name)}
        >
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M9 12l2 2 4-4"/>
            <path d="M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z"/>
          </svg>
          {t('evidenceProveSkill')}
        </button>
      )}
    </div>
  );
}
