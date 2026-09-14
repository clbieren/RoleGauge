'use client';

import React from 'react';
import styles from './AdPlacement.module.css';

export interface AdPlacementProps {
  slot: 'loading_screen' | 'results_sidebar_left' | 'results_sidebar_right';
  enabled?: boolean;
  locale?: string;
  className?: string;
}

export default function AdPlacement({
  slot,
  enabled = true,
  locale = 'tr',
  className = '',
}: AdPlacementProps) {
  if (!enabled) return null;

  const isTr = locale === 'tr';

  if (slot === 'loading_screen') {
    return (
      <aside
        className={`${styles.adContainer} ${styles.loadingBanner} ${className}`}
        aria-label="Sponsored placement"
      >
        <span className={styles.adBadge}>{isTr ? 'Sponsorlu' : 'Sponsored'}</span>
        <div className={styles.adIcon}>🚀</div>
        <div className={styles.adContent}>
          <div className={styles.adTitle}>
            {isTr
              ? 'Yeteneklerinize Göre Küresel Kariyer Fırsatları'
              : 'Global Tech Careers Matched to Your Skills'}
          </div>
          <div className={styles.adText}>
            {isTr
              ? 'Doğrulanmış yetkinliklerinizle doğrudan eşleşen uzaktan mühendislik rollerini keşfedin.'
              : 'Explore high-growth remote engineering roles matching your verified skill benchmark.'}
          </div>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className={styles.adAction}
          >
            {isTr ? 'İlanları İncele →' : 'Explore Roles →'}
          </a>
        </div>
      </aside>
    );
  }

  if (slot === 'results_sidebar_left') {
    return (
      <aside
        className={`${styles.adContainer} ${styles.sidebarBanner} ${className}`}
        aria-label="Sponsored career partner"
      >
        <span className={styles.adBadge}>{isTr ? 'Öne Çıkan' : 'Partner'}</span>
        <div className={styles.adIcon}>💼</div>
        <div className={styles.adContent}>
          <div className={styles.adTitle}>
            {isTr ? 'Kıdemli Pozisyonlar İçin Mülakat Hazırlığı' : 'Master Senior Tech Interviews'}
          </div>
          <div className={styles.adText}>
            {isTr
              ? 'Sistem tasarımı ve mimari odaklı pratiklerle hedeflenen role adım atın.'
              : 'Targeted system design & architecture prep to crack top-tier technical interviews.'}
          </div>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className={styles.adAction}
          >
            {isTr ? 'Detayları Gör →' : 'Learn More →'}
          </a>
        </div>
      </aside>
    );
  }

  if (slot === 'results_sidebar_right') {
    return (
      <aside
        className={`${styles.adContainer} ${styles.sidebarBanner} ${className}`}
        aria-label="Sponsored learning track"
      >
        <span className={styles.adBadge}>{isTr ? 'Gelişim' : 'Level Up'}</span>
        <div className={styles.adIcon}>⚡</div>
        <div className={styles.adContent}>
          <div className={styles.adTitle}>
            {isTr ? 'Eksik Becerileri Tamamlama Rehberi' : 'Accelerate Missing Skills'}
          </div>
          <div className={styles.adText}>
            {isTr
              ? 'Skor kartınızda tespit edilen boşlukları kapatacak uygulamalı mühendislik projeleri.'
              : 'Hands-on production projects to bridge identified skill gaps in your profile.'}
          </div>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className={styles.adAction}
          >
            {isTr ? 'Rehbere Başla →' : 'Start Track →'}
          </a>
        </div>
      </aside>
    );
  }

  return null;
}
