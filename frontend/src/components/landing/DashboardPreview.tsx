'use client';

import React, { useState } from 'react';
import { TranslationKey } from '@/lib/i18n';
import styles from './DashboardPreview.module.css';

interface DashboardPreviewProps {
  t: (key: TranslationKey) => string;
  onExploreClick?: () => void;
}

type RoleKey = 'game' | 'backend' | 'frontend';

export default function DashboardPreview({ t, onExploreClick }: DashboardPreviewProps) {
  const [topRole, setTopRole] = useState<RoleKey>('game');

  // Compute display order so topRole is always at index 0 (front), others behind
  const allRoles: RoleKey[] = ['game', 'backend', 'frontend'];
  const otherRoles = allRoles.filter(r => r !== topRole);
  const orderedRoles: RoleKey[] = [topRole, otherRoles[0], otherRoles[1]];

  const cardData: Record<
    RoleKey,
    {
      fileTitle: string;
      username: string;
      initials: string;
      roleName: string;
      level: string;
      score: number;
      tier: string;
      pillClass: string;
      reposCount: string;
      provenance: string;
      skills: { name: string; score: number }[];
    }
  > = {
    game: {
      fileTitle: 'gamedev_eval.lens',
      username: '@demo-gamedev',
      initials: 'GD',
      roleName: t('previewGameRole'),
      level: t('previewGameLevel'),
      score: 84,
      tier: t('previewReady'),
      pillClass: styles.pillReady,
      reposCount: t('previewGameRepos'),
      provenance: t('previewGameProvenance'),
      skills: [
        { name: t('previewGameSkill1'), score: 88 },
        { name: t('previewGameSkill2'), score: 85 },
        { name: t('previewGameSkill3'), score: 78 },
        { name: t('previewGameSkill4'), score: 82 },
      ],
    },
    backend: {
      fileTitle: 'backend_eval.lens',
      username: '@demo-backend',
      initials: 'BE',
      roleName: t('previewBackendRole'),
      level: t('previewBackendLevel'),
      score: 91,
      tier: t('tierExceeds'),
      pillClass: styles.pillExceeds,
      reposCount: t('previewBackendRepos'),
      provenance: t('previewBackendProvenance'),
      skills: [
        { name: t('previewBackendSkill1'), score: 94 },
        { name: t('previewBackendSkill2'), score: 92 },
        { name: t('previewBackendSkill3'), score: 88 },
        { name: t('previewBackendSkill4'), score: 90 },
      ],
    },
    frontend: {
      fileTitle: 'frontend_eval.lens',
      username: '@demo-frontend',
      initials: 'FE',
      roleName: t('previewFrontendRole'),
      level: t('previewFrontendLevel'),
      score: 76,
      tier: t('previewReady'),
      pillClass: styles.pillReady,
      reposCount: t('previewFrontendRepos'),
      provenance: t('previewFrontendProvenance'),
      skills: [
        { name: t('previewFrontendSkill1'), score: 85 },
        { name: t('previewFrontendSkill2'), score: 78 },
        { name: t('previewFrontendSkill3'), score: 72 },
        { name: t('previewFrontendSkill4'), score: 70 },
      ],
    },
  };

  const slotClasses = [styles.slotFront, styles.slotMid, styles.slotBack];

  return (
    <div className={styles.showcaseWrapper}>
      {/* Top Header with demo badge & profile tabs */}
      <div className={styles.showcaseHeader}>
        <span className={styles.demoTag}>
          ◈ {t('previewDemoBadge')}
        </span>

        <div className={styles.tabsGroup} role="tablist" aria-label="Demo role selector">
          <button
            type="button"
            className={`${styles.tabBtn} ${topRole === 'game' ? styles.tabBtnActive : ''}`}
            onClick={() => setTopRole('game')}
            role="tab"
            aria-selected={topRole === 'game'}
          >
            {t('previewTabGame')}
          </button>
          <button
            type="button"
            className={`${styles.tabBtn} ${topRole === 'backend' ? styles.tabBtnActive : ''}`}
            onClick={() => setTopRole('backend')}
            role="tab"
            aria-selected={topRole === 'backend'}
          >
            {t('previewTabBackend')}
          </button>
          <button
            type="button"
            className={`${styles.tabBtn} ${topRole === 'frontend' ? styles.tabBtnActive : ''}`}
            onClick={() => setTopRole('frontend')}
            role="tab"
            aria-selected={topRole === 'frontend'}
          >
            {t('previewTabFrontend')}
          </button>
        </div>
      </div>

      {/* Cascading overlapping mini windows stage */}
      <div className={styles.stage}>
        {orderedRoles.map((roleKey, slotIndex) => {
          const item = cardData[roleKey];
          const isFront = slotIndex === 0;

          return (
            <div
              key={roleKey}
              className={`${styles.windowCard} ${slotClasses[slotIndex]}`}
              onClick={() => {
                if (!isFront) setTopRole(roleKey);
              }}
              role="region"
              aria-label={`${item.roleName} Demo Window`}
            >
              {/* Window Title Bar */}
              <div className={styles.windowHeader}>
                <div className={styles.windowControls}>
                  <span className={styles.dotRed} />
                  <span className={styles.dotYellow} />
                  <span className={styles.dotGreen} />
                </div>
                <span className={styles.windowTitle}>{item.fileTitle}</span>
                <span className={`${styles.windowPill} ${item.pillClass}`}>
                  {item.score}% · {item.tier}
                </span>
              </div>

              {/* Window Content */}
              <div className={styles.windowBody}>
                {/* Profile row */}
                <div className={styles.profileRow}>
                  <div className={styles.avatar}>
                    <span>{item.initials}</span>
                  </div>
                  <div className={styles.userMeta}>
                    <div className={styles.username}>
                      <span>{item.username}</span>
                      <span className={styles.liveDot} title="Verified demo profile" />
                    </div>
                    <span className={styles.roleLevel}>
                      {item.roleName} · {item.level}
                    </span>
                  </div>
                </div>

                {/* Score Banner */}
                <div className={styles.scoreBanner}>
                  <div>
                    <div className={styles.scoreLabel}>{t('previewReadiness')}</div>
                    <div className={styles.reposScanned}>{item.reposCount}</div>
                  </div>
                  <div className={styles.scoreNumber}>
                    {item.score}<span className={styles.scorePercent}>%</span>
                  </div>
                </div>

                {/* Skills progress list */}
                <div className={styles.skillsList}>
                  {item.skills.map(skill => (
                    <div key={skill.name} className={styles.skillRow}>
                      <div className={styles.skillTop}>
                        <span className={styles.skillTitle}>{skill.name}</span>
                        <span className={styles.skillScore}>{skill.score}%</span>
                      </div>
                      <div className={styles.barTrack}>
                        <div
                          className={styles.barFill}
                          style={{ width: `${skill.score}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>

                {/* Footer */}
                <div className={styles.windowFooter}>
                  <span className={styles.codeBadge}>{item.provenance}</span>
                  <button
                    type="button"
                    className={styles.openSampleBtn}
                    onClick={e => {
                      e.stopPropagation();
                      if (onExploreClick) onExploreClick();
                    }}
                  >
                    {t('previewFullReportBtn')} →
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
