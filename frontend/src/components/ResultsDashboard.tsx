'use client';

import { AnalyzeResponse } from '@/lib/api';
import ReadinessGauge from './ReadinessGauge';
import SkillRadarChart from './SkillRadarChart';
import SubskillGrid from './SubskillGrid';
import RepoBreakdown from './RepoBreakdown';
import styles from './ResultsDashboard.module.css';

interface ResultsDashboardProps {
  result: AnalyzeResponse;
  onReset: () => void;
}

export default function ResultsDashboard({ result, onReset }: ResultsDashboardProps) {
  const relevantRepos = result.repos.filter(r => r.is_relevant);

  return (
    <div className="dashboard">
      <div className="container">
        {/* Header */}
        <div className="dashboard-header animate-fade-in">
          <img
            src={`https://github.com/${result.github_username}.png?size=64`}
            alt={result.github_username}
            className={styles.headerAvatar}
            onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
          />
          <div className={styles.headerInfo}>
            <h1 className={styles.headerTitle}>
              @{result.github_username}
              <span className={styles.headerBadge}>{result.role_name}</span>
            </h1>
            <p className={styles.headerMeta}>
              {result.total_repos_scanned} repo tarandı · {result.relevant_repos_found} ilgili bulundu
            </p>
          </div>
          <button className="btn btn-ghost" onClick={onReset}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
              <path d="M3 3v5h5"/>
            </svg>
            Yeni Analiz
          </button>
        </div>

        {/* Top Row: Gauge + Radar */}
        <div className="dashboard-grid">
          <div className="glass-card animate-fade-in-up" style={{ padding: '32px', animationDelay: '0.1s' }}>
            <h2 className={styles.sectionTitle}>Hazırlık Skoru</h2>
            <ReadinessGauge
              score={result.readiness_score}
              tier={result.readiness_tier}
              label={result.readiness_label}
            />
          </div>
          <div className="glass-card animate-fade-in-up" style={{ padding: '32px', animationDelay: '0.2s' }}>
            <h2 className={styles.sectionTitle}>Skill Dağılımı</h2>
            <SkillRadarChart skills={result.skills} />
          </div>
        </div>

        {/* Subskill Grid */}
        <div className="glass-card animate-fade-in-up" style={{ padding: '32px', marginBottom: '24px', animationDelay: '0.3s' }}>
          <h2 className={styles.sectionTitle}>Subskill Detayları</h2>
          <SubskillGrid skills={result.skills} />
        </div>

        {/* Repo Breakdown */}
        {relevantRepos.length > 0 && (
          <div className="glass-card animate-fade-in-up" style={{ padding: '32px', marginBottom: '32px', animationDelay: '0.4s' }}>
            <h2 className={styles.sectionTitle}>Repo Analizi</h2>
            <RepoBreakdown repos={result.repos} />
          </div>
        )}
      </div>
    </div>
  );
}
