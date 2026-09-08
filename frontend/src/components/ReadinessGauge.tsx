'use client';
import { useEffect, useState } from 'react';
import { useLocale } from '@/lib/useLocale';
import { tTierLabel, tReadinessDesc } from '@/lib/i18n';
import styles from './ReadinessGauge.module.css';

interface ReadinessGaugeProps {
  score: number;   // 0.0 – 1.0
  tier: string;
  label: string;
}

const TIER_COLOR: Record<string, string> = {
  not_ready:   'var(--tier-not_ready)',
  developing:  'var(--tier-developing)',
  approaching: 'var(--tier-approaching)',
  ready:       'var(--tier-ready)',
  exceeds:     'var(--tier-exceeds)',
};

const TIER_CLASS: Record<string, string> = {
  not_ready:   'tier-not_ready',
  developing:  'tier-developing',
  approaching: 'tier-approaching',
  ready:       'tier-ready',
  exceeds:     'tier-exceeds',
};

export default function ReadinessGauge({ score, tier }: ReadinessGaugeProps) {
  const { locale } = useLocale();
  const [displayed, setDisplayed] = useState(0);
  const target = Math.round(score * 100);

  // Animate number on mount
  useEffect(() => {
    const start = Date.now();
    const duration = 900;
    const raf = () => {
      const p = Math.min((Date.now() - start) / duration, 1);
      // ease-out cubic
      const eased = 1 - Math.pow(1 - p, 3);
      setDisplayed(Math.round(eased * target));
      if (p < 1) requestAnimationFrame(raf);
    };
    requestAnimationFrame(raf);
  }, [target]);

  const color = TIER_COLOR[tier] ?? 'var(--text-primary)';
  const tierClass = TIER_CLASS[tier] ?? '';
  const desc = tReadinessDesc(tier, locale);

  return (
    <div className={styles.container}>
      {/* Score number */}
      <div className={styles.scoreRow}>
        <span className={styles.scoreNum} style={{ color }}>
          {displayed}
        </span>
        <span className={styles.scoreUnit}>/ 100</span>
      </div>

      {/* Tier badge */}
      <span className={`badge ${tierClass} ${styles.tierBadge}`}>
        {tTierLabel(tier, locale)}
      </span>

      {/* Description */}
      {desc && <p className={styles.desc}>{desc}</p>}

      {/* Thin linear bar */}
      <div className={styles.bar}>
        <div
          className={styles.barFill}
          style={{ width: `${target}%`, background: color }}
        />
      </div>
    </div>
  );
}
