'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { UserAnalysisSummary, getMyAnalyses } from '@/lib/api';
import { useAuth } from '@/context/AuthContext';
import { useLocale } from '@/lib/useLocale';
import { formatDate } from '@/lib/i18n';
import AuthModal from '@/components/AuthModal';
import styles from './history.module.css';

export default function HistoryPage() {
  const { user, token, isAuthenticated, logout, openAuthModal } = useAuth();
  const { locale } = useLocale();

  const [analyses, setAnalyses] = useState<UserAnalysisSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!isAuthenticated || !token) return;

    getMyAnalyses(token)
      .then((data) => {
        setAnalyses(data);
        setError('');
      })
      .catch((err) => {
        setError(err.message || 'Geçmiş analizler yüklenemedi');
      })
      .finally(() => {
        setLoading(false);
      });
  }, [isAuthenticated, token]);

  const showLoading = isAuthenticated && Boolean(token) && loading;

  const getTierClass = (tier: string) => {
    switch (tier?.toLowerCase()) {
      case 'ready':
        return styles.tier_ready;
      case 'almost_ready':
        return styles.tier_almost_ready;
      case 'development_needed':
        return styles.tier_development_needed;
      default:
        return styles.tier_not_recommended;
    }
  };

  return (
    <div className={styles.page}>
      {/* Navigation Header */}
      <nav className={styles.nav}>
        <div className={styles.navInner}>
          <Link href="/" className={styles.logo}>
            <span className={styles.logoMark}>◈</span>
            SkillLens
          </Link>
          <div className={styles.navRight}>
            <Link href="/" className={styles.newAnalysisBtn}>
              + Yeni Analiz
            </Link>
            {isAuthenticated && user && (
              <>
                <div className={styles.userBadge}>
                  <span className={styles.userDot} />
                  <span>{user.full_name || user.email.split('@')[0]}</span>
                </div>
                <button className={styles.logoutBtn} onClick={logout}>
                  Çıkış
                </button>
              </>
            )}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className={styles.container}>
        <div className={styles.header}>
          <h1 className={styles.title}>Analiz Geçmişi</h1>
          <p className={styles.subtitle}>
            Hesabınızla gerçekleştirdiğiniz geçmiş değerlendirmelerin listesi ve sonuçları.
          </p>
        </div>

        {!isAuthenticated ? (
          <div className={styles.authPrompt}>
            <div className={styles.emptyIcon}>🔒</div>
            <h2 className={styles.emptyTitle}>Giriş Yapılması Gerekiyor</h2>
            <p className={styles.emptyText}>
              Geçmiş analizlerinizi ve detaylı gelişim raporlarınızı görüntülemek için lütfen hesabınıza giriş yapın.
            </p>
            <button className={styles.primaryBtn} onClick={() => openAuthModal('login')}>
              Giriş Yap / Kayıt Ol
            </button>
          </div>
        ) : showLoading ? (
          <div className={styles.emptyState}>
            <p className={styles.emptyText}>Analiz geçmişiniz yükleniyor...</p>
          </div>
        ) : error ? (
          <div className={styles.emptyState}>
            <p className={styles.emptyText} style={{ color: '#ef4444' }}>{error}</p>
          </div>
        ) : analyses.length === 0 ? (
          <div className={styles.emptyState}>
            <div className={styles.emptyIcon}>📂</div>
            <h2 className={styles.emptyTitle}>Henüz Kayıtlı Analiz Yok</h2>
            <p className={styles.emptyText}>
              Giriş yaptıktan sonra çalıştırdığınız tüm profil ve CV analizleri burada arşivlenecektir.
            </p>
            <Link href="/" className={styles.primaryBtn}>
              İlk Analizi Başlat
            </Link>
          </div>
        ) : (
          <div className={styles.cardGrid}>
            {analyses.map((item) => {
              const isCv = item.github_username === 'cv_upload' || item.github_username === 'linkedin_upload';
              return (
                <Link
                  key={item.id}
                  href={`/results/${item.id}`}
                  className={styles.analysisCard}
                >
                  <div className={styles.cardLeft}>
                    <div className={styles.sourceIcon}>
                      {isCv ? '📄' : '🐙'}
                    </div>
                    <div className={styles.cardDetails}>
                      <span className={styles.roleTitle}>
                        {item.role_name}
                      </span>
                      <div className={styles.cardMeta}>
                        <span className={styles.metaCandidate}>
                          {item.github_username}
                        </span>
                        <span className={styles.metaDot}>•</span>
                        <span>{item.level.toUpperCase()}</span>
                        <span className={styles.metaDot}>•</span>
                        <span>{formatDate(item.created_at, locale)}</span>
                      </div>
                    </div>
                  </div>

                  <div className={styles.cardRight}>
                    <div className={styles.scoreGroup}>
                      <div className={`${styles.scoreVal} ${getTierClass(item.readiness_tier)}`}>
                        {Math.round(item.readiness_score)}%
                      </div>
                      <div className={`${styles.tierLabel} ${getTierClass(item.readiness_tier)}`}>
                        {item.readiness_label || item.readiness_tier}
                      </div>
                    </div>
                    <span className={styles.arrow}>→</span>
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </main>

      <AuthModal locale={locale} />
    </div>
  );
}
