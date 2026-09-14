'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { AnalyzeResponse, fetchResult } from '@/lib/api';
import { SAMPLE_ANALYSIS } from '@/lib/sampleAnalysis';
import ResultsDashboard from '@/components/ResultsDashboard';
import { useAuth } from '@/context/AuthContext';
import styles from './results.module.css';

export default function ResultDetailPage() {
  const params = useParams();
  const router = useRouter();
  const { token } = useAuth();

  const id = typeof params?.id === 'string' ? params.id : Array.isArray(params?.id) ? params.id[0] : '';

  const [result, setResult] = useState<AnalyzeResponse | null>(() =>
    id === 'sample-demo-analysis' ? SAMPLE_ANALYSIS : null
  );
  const [loading, setLoading] = useState<boolean>(() => id !== 'sample-demo-analysis');
  const [error, setError] = useState('');

  useEffect(() => {
    if (!id || id === 'sample-demo-analysis') return;

    fetchResult(id, token || undefined)
      .then((data) => {
        setResult(data);
      })
      .catch((err) => {
        setError(err.message || 'Analiz sonucu yüklenemedi');
      })
      .finally(() => {
        setLoading(false);
      });
  }, [id, token]);

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.centerState}>
          <div className={styles.spinner} />
          <p className={styles.loadingText}>Analiz sonucu yükleniyor...</p>
        </div>
      </div>
    );
  }

  if (error || !result) {
    return (
      <div className={styles.container}>
        <div className={styles.centerState}>
          <div className={styles.errorCard}>
            <div className={styles.errorIcon}>⚠</div>
            <h2 className={styles.errorTitle}>Sonuç Bulunamadı</h2>
            <p className={styles.errorDetail}>
              {error || 'İstenen analiz sonucu mevcut değil veya erişim izniniz bulunmuyor.'}
            </p>
            <button className={styles.homeBtn} onClick={() => router.push('/')}>
              Ana Sayfaya Dön
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <ResultsDashboard
      result={result}
      onReset={() => router.push('/')}
    />
  );
}
