'use client';

import { useEffect, useRef, useState } from 'react';
import styles from './ReadinessGauge.module.css';

interface ReadinessGaugeProps {
  score: number;
  tier: string;
  label: string;
}

const TIER_CONFIG: Record<string, { color: string; gradient: string }> = {
  not_ready: { color: '#ef4444', gradient: 'linear-gradient(135deg, #ef4444, #dc2626)' },
  developing: { color: '#f97316', gradient: 'linear-gradient(135deg, #f97316, #ea580c)' },
  approaching: { color: '#eab308', gradient: 'linear-gradient(135deg, #eab308, #ca8a04)' },
  ready: { color: '#22c55e', gradient: 'linear-gradient(135deg, #22c55e, #16a34a)' },
  exceeds: { color: '#6366f1', gradient: 'linear-gradient(135deg, #6366f1, #8b5cf6)' },
};

export default function ReadinessGauge({ score, tier, label }: ReadinessGaugeProps) {
  const [displayScore, setDisplayScore] = useState(0);
  const config = TIER_CONFIG[tier] || TIER_CONFIG.not_ready;

  // Animate score count-up
  useEffect(() => {
    const target = Math.round(score * 100);
    const duration = 1200;
    const startTime = Date.now();

    const animate = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplayScore(Math.round(eased * target));

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
  }, [score]);

  const percentage = score * 100;
  const circumference = 2 * Math.PI * 88;
  const offset = circumference - (percentage / 100) * circumference * 0.75; // 270 degree arc

  return (
    <div className={styles.container}>
      <div className={styles.gaugeWrapper}>
        <svg viewBox="0 0 200 200" className={styles.gaugeSvg}>
          {/* Background arc */}
          <circle
            cx="100"
            cy="100"
            r="88"
            fill="none"
            stroke="rgba(255,255,255,0.05)"
            strokeWidth="10"
            strokeLinecap="round"
            strokeDasharray={`${circumference * 0.75} ${circumference * 0.25}`}
            transform="rotate(135 100 100)"
          />
          {/* Value arc */}
          <circle
            cx="100"
            cy="100"
            r="88"
            fill="none"
            stroke={config.color}
            strokeWidth="10"
            strokeLinecap="round"
            strokeDasharray={`${circumference * 0.75} ${circumference * 0.25}`}
            strokeDashoffset={offset}
            transform="rotate(135 100 100)"
            className={styles.valueArc}
            style={{
              filter: `drop-shadow(0 0 8px ${config.color}50)`,
            }}
          />
        </svg>
        <div className={styles.gaugeCenter}>
          <span className={`${styles.scoreValue} mono`} style={{ color: config.color }}>
            {displayScore}
          </span>
          <span className={styles.scoreUnit}>/ 100</span>
        </div>
      </div>
      <div
        className={styles.tierBadge}
        style={{
          background: `${config.color}18`,
          borderColor: `${config.color}40`,
          color: config.color,
        }}
      >
        {label}
      </div>
    </div>
  );
}
