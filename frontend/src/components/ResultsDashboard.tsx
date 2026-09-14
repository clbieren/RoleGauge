'use client';

import { useState } from 'react';
import { AnalyzeResponse } from '@/lib/api';
import ReadinessGauge from './ReadinessGauge';
import SkillsOverview from './SkillsOverview';
import SubskillGrid from './SubskillGrid';
import RepoBreakdown from './RepoBreakdown';
import AssessmentModal from './AssessmentModal';
import AdPlacement from './AdPlacement';
import styles from './ResultsDashboard.module.css';
import { useLocale } from '@/lib/useLocale';
import { formatDate, tLevelLabel } from '@/lib/i18n';

interface ResultsDashboardProps {
  result: AnalyzeResponse;
  onReset: () => void;
}

export default function ResultsDashboard({ result, onReset }: ResultsDashboardProps) {
  const { locale, toggle, t } = useLocale();
  const [dashboardResult, setDashboardResult] = useState<AnalyzeResponse>(result);
  const [activeAssessment, setActiveAssessment] = useState<{
    compositeKey: string;
    subskillName: string;
  } | null>(null);

  const totalFiles = dashboardResult.repos.reduce(
    (sum, r) => sum + r.relevant_files_count,
    0
  );
  const coreSkillsEvidenced = dashboardResult.skills.filter(
    s => s.subskills.some(sub => sub.status === 'evidence_found')
  ).length;

  const isCvUpload =
    dashboardResult.github_username === 'cv_upload' ||
    dashboardResult.github_username === 'linkedin_upload';

  const showLeftAd = Boolean(dashboardResult.ad_placements?.results_sidebar_left);
  const showRightAd = Boolean(dashboardResult.ad_placements?.results_sidebar_right);

  return (
    <div className={styles.page}>
      {/* Navbar */}
      <nav className={styles.nav}>
        <div className={styles.navInner}>
          <button className={styles.logo} onClick={onReset}>
            <span className={styles.logoMark}>◈</span>
            SkillLens
          </button>
          <div className={styles.navRight}>
            <button className={styles.navBtn} onClick={onReset}>
              {t('navNewAnalysis')}
            </button>
            {/* Locale toggle */}
            <div className={styles.localePill}>
              <button
                className={`${styles.localeBtn} ${locale === 'tr' ? styles.localeBtnActive : ''}`}
                onClick={() => locale !== 'tr' && toggle()}
              >
                TR
              </button>
              <button
                className={`${styles.localeBtn} ${locale === 'en' ? styles.localeBtnActive : ''}`}
                onClick={() => locale !== 'en' && toggle()}
              >
                EN
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className={styles.content}>
        {dashboardResult.id === 'sample-demo-analysis' && (
          <div className={styles.demoBanner}>
            <span className={styles.demoDot} />
            <span>{t('demoBannerLabel')}</span>
          </div>
        )}

        {/* Page title */}
        <div className={styles.pageTitle}>
          <p className={styles.pageTitleRole}>
            {dashboardResult.role_name.replace(/^(Junior|Mid|Senior)\s+/i, '')} · {tLevelLabel(dashboardResult.level, locale)}
          </p>
          <p className={styles.pageTitleMeta}>
            {t('dashboardAnalyzedOn')} {formatDate(dashboardResult.created_at, locale)}
          </p>
        </div>

        {/* Main Content Layout with Ad Sidebars */}
        <div className={styles.layoutWithAds}>
          {showLeftAd && (
            <div className={styles.sidebarCol}>
              <AdPlacement
                slot="results_sidebar_left"
                enabled={showLeftAd}
                locale={locale}
              />
            </div>
          )}

          <div className={styles.mainCol}>
            {/* Hero card — profile left / readiness right */}
            <div className={styles.heroCard}>
          {/* Left: profile + stats */}
          <div className={styles.heroLeft}>
            <div className={styles.profileRow}>
              {isCvUpload ? (
                <div className={styles.cvAvatar}>📄</div>
              ) : (
                <div className={styles.avatar}>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img
                    src={`https://github.com/${dashboardResult.github_username}.png?size=80`}
                    alt={dashboardResult.github_username}
                    className={styles.avatarImg}
                    onError={e => {
                      (e.target as HTMLImageElement).style.display = 'none';
                    }}
                  />
                </div>
              )}
              <div>
                <p className={styles.profileName}>
                  {isCvUpload
                    ? (locale === 'tr' ? 'Özgeçmiş / Profil Dosyası' : 'Uploaded Profile / CV')
                    : `@${dashboardResult.github_username}`}
                </p>
                <p className={styles.profileRole}>
                  {dashboardResult.role_name.replace(/^(Junior|Mid|Senior)\s+/i, '')}
                </p>
              </div>
            </div>

            <div className={styles.heroStats}>
              {dashboardResult.total_repos_scanned > 0 ? (
                <>
                  <div className={styles.heroStat}>
                    <span className={styles.heroStatVal}>{dashboardResult.total_repos_scanned}</span>
                    <span className={styles.heroStatLabel}>{t('dashboardRepoCount')}</span>
                  </div>
                  {totalFiles > 0 && (
                    <div className={styles.heroStat}>
                      <span className={styles.heroStatVal}>
                        {totalFiles.toLocaleString()}
                      </span>
                      <span className={styles.heroStatLabel}>{t('dashboardFilesReviewed')}</span>
                    </div>
                  )}
                  <div className={styles.heroStat}>
                    <span className={styles.heroStatVal}>{dashboardResult.relevant_repos_found}</span>
                    <span className={styles.heroStatLabel}>
                      {t('dashboardRelevantRepos')}
                    </span>
                  </div>
                </>
              ) : (
                <>
                  <div className={styles.heroStat}>
                    <span className={styles.heroStatVal}>{dashboardResult.skills.length}</span>
                    <span className={styles.heroStatLabel}>
                      {locale === 'tr' ? 'Değerlendirilen Beceri' : 'Skills Assessed'}
                    </span>
                  </div>
                  <div className={styles.heroStat}>
                    <span className={styles.heroStatVal}>{coreSkillsEvidenced}</span>
                    <span className={styles.heroStatLabel}>
                      {locale === 'tr' ? 'Kanıtlanan Beceri' : 'Skills Evidenced'}
                    </span>
                  </div>
                  <div className={styles.heroStat}>
                    <span className={styles.heroStatVal}>
                      {dashboardResult.github_username === 'linkedin_upload' ? 'LinkedIn' : 'CV / Resume'}
                    </span>
                    <span className={styles.heroStatLabel}>
                      {locale === 'tr' ? 'Veri Kaynağı' : 'Data Source'}
                    </span>
                  </div>
                </>
              )}
            </div>
          </div>

          {/* Right: readiness score */}
          <div className={styles.heroRight}>
            <p className={styles.heroReadinessLabel}>{t('dashboardReadiness')}</p>
            <ReadinessGauge
              score={dashboardResult.readiness_score}
              tier={dashboardResult.readiness_tier}
              label={dashboardResult.readiness_label}
            />
          </div>
        </div>

        {/* Summary cards */}
        <div className={styles.summaryGrid}>
          <div className={styles.summaryCard}>
            <span className={styles.summaryVal}>{dashboardResult.total_repos_scanned}</span>
            <span className={styles.summaryLabel}>{t('summaryRepositories')}</span>
          </div>
          <div className={styles.summaryCard}>
            <span className={styles.summaryVal}>{dashboardResult.skills.length}</span>
            <span className={styles.summaryLabel}>{t('summarySkills')}</span>
          </div>
          <div className={styles.summaryCard}>
            <span className={styles.summaryVal}>
              {coreSkillsEvidenced} / {dashboardResult.skills.length}
            </span>
            <span className={styles.summaryLabel}>{t('summaryCoreSkills')}</span>
          </div>
        </div>

        {/* Skills Overview */}
        <div className={styles.sectionBlock}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>{t('skillsOverviewTitle')}</h2>
          </div>
          <div className={styles.sectionContent}>
            <SkillsOverview skills={dashboardResult.skills} />
          </div>
        </div>

        {/* Skills Breakdown */}
        <div className={styles.sectionBlock}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>{t('skillsBreakdownTitle')}</h2>
          </div>
          <div className={styles.sectionContent}>
            <SubskillGrid
              skills={dashboardResult.skills}
              onProveSkill={(compositeKey, subskillName) =>
                setActiveAssessment({ compositeKey, subskillName })
              }
            />
          </div>
        </div>

        {/* Repositories */}
        {dashboardResult.repos.length > 0 && (
          <div className={styles.sectionBlock}>
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>{t('reposTitle')}</h2>
            </div>
            <div className={styles.sectionContent}>
              <RepoBreakdown repos={dashboardResult.repos} />
            </div>
          </div>
        )}
          </div>

          {showRightAd && (
            <div className={styles.sidebarCol}>
              <AdPlacement
                slot="results_sidebar_right"
                enabled={showRightAd}
                locale={locale}
              />
            </div>
          )}
        </div>
      </div>

      {/* Interactive Assessment Modal */}
      {activeAssessment && (
        <AssessmentModal
          analysisId={dashboardResult.id}
          compositeKey={activeAssessment.compositeKey}
          subskillName={activeAssessment.subskillName}
          currentReadinessScore={dashboardResult.readiness_score}
          locale={locale}
          onClose={() => setActiveAssessment(null)}
          onSuccess={updated => {
            setDashboardResult(updated);
            try {
              localStorage.setItem('skilllens_last_result', JSON.stringify(updated));
            } catch {
              // ignore
            }
          }}
        />
      )}
    </div>
  );
}
