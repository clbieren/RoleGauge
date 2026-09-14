'use client';

import { useState, useEffect } from 'react';
import {
  AnalyzeResponse,
  AssessmentQuestion,
  AssessmentQuestionEvaluation,
  startAssessment,
  submitAssessment,
} from '@/lib/api';
import { getTranslatedQuestion } from '@/lib/questionTranslations';
import { tSubskillName } from '@/lib/skillTranslations';
import styles from './AssessmentModal.module.css';

interface AssessmentModalProps {
  analysisId: string;
  compositeKey: string;
  subskillName: string;
  currentReadinessScore?: number;
  onClose: () => void;
  onSuccess: (updatedAnalysis: AnalyzeResponse) => void;
  locale: string;
}

export default function AssessmentModal({
  analysisId,
  compositeKey,
  subskillName,
  currentReadinessScore,
  onClose,
  onSuccess,
  locale,
}: AssessmentModalProps) {
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [sessionId, setSessionId] = useState('');
  const [question, setQuestion] = useState<AssessmentQuestion | null>(null);
  const [answer, setAnswer] = useState('');
  const [questionLang, setQuestionLang] = useState<'tr' | 'en'>(locale === 'tr' ? 'tr' : 'en');
  const [evaluation, setEvaluation] = useState<AssessmentQuestionEvaluation | null>(null);
  const [updatedAnalysis, setUpdatedAnalysis] = useState<AnalyzeResponse | null>(null);
  const [scoreDelta, setScoreDelta] = useState<{ prev: number; updated: number } | null>(null);

  useEffect(() => {
    let isMounted = true;

    startAssessment(analysisId, compositeKey)
      .then(res => {
        if (!isMounted) return;
        if (res.questions && res.questions.length > 0) {
          setSessionId(res.assessment_session_id);
          setQuestion(res.questions[0]);
        } else {
          setError(
            locale === 'tr'
              ? 'Bu beceri için henüz değerlendirme sorusu bulunamadı.'
              : 'No assessment questions found for this skill yet.'
          );
        }
      })
      .catch(err => {
        if (!isMounted) return;
        setError(
          err instanceof Error
            ? err.message
            : locale === 'tr'
            ? 'Değerlendirme başlatılamadı.'
            : 'Failed to start assessment.'
        );
      })
      .finally(() => {
        if (isMounted) setLoading(false);
      });

    return () => {
      isMounted = false;
    };
  }, [analysisId, compositeKey, locale]);

  const handleSubmit = async () => {
    if (!sessionId || !question || !answer.trim() || submitting) return;

    setSubmitting(true);
    setError('');

    try {
      const res = await submitAssessment(sessionId, {
        [question.composite_key]: answer.trim(),
      });

      if (res.evaluations && res.evaluations.length > 0) {
        setEvaluation(res.evaluations[0]);
      }

      if (res.updated_analysis) {
        setUpdatedAnalysis(res.updated_analysis);
        const prev = Math.round((currentReadinessScore ?? res.updated_analysis.readiness_score) * 100);
        const updated = Math.round(res.updated_analysis.readiness_score * 100);
        setScoreDelta({ prev, updated });
      }
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : locale === 'tr'
          ? 'Cevap gönderilemedi.'
          : 'Failed to submit answer.'
      );
    } finally {
      setSubmitting(false);
    }
  };

  const handleFinish = () => {
    if (updatedAnalysis) {
      onSuccess(updatedAnalysis);
    }
    onClose();
  };

  return (
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className={styles.header}>
          <div className={styles.headerTitleWrap}>
            <span className={styles.headerCategory}>
              {locale === 'tr' ? 'Teknik Değerlendirme' : 'Technical Assessment'}
            </span>
            <h3 className={styles.headerTitle}>{tSubskillName(subskillName, locale)}</h3>
          </div>
          <button
            type="button"
            className={styles.closeBtn}
            onClick={onClose}
            aria-label={locale === 'tr' ? 'Kapat' : 'Close'}
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>

        {/* Body */}
        <div className={styles.body}>
          {loading && (
            <div className={styles.centerBox}>
              <span className="spinner" style={{ width: 24, height: 24 }} />
              <p className={styles.centerText}>
                {locale === 'tr'
                  ? 'Değerlendirme sorusu hazırlanıyor...'
                  : 'Preparing assessment question...'}
              </p>
            </div>
          )}

          {error && !loading && (
            <div className={styles.centerBox}>
              <p style={{ color: 'var(--danger)', fontSize: '0.9rem' }}>{error}</p>
            </div>
          )}

          {/* Question / Answering State */}
          {!loading && !error && question && !evaluation && (
            <>
              <div className={styles.questionBox}>
                <div className={styles.questionHeader}>
                  <div className={styles.questionMeta}>
                    <span className={styles.typeBadge}>
                      {question.type} · {question.level}
                    </span>
                  </div>
                  <div className={styles.langToggle}>
                    <button
                      type="button"
                      className={`${styles.langBtn} ${questionLang === 'tr' ? styles.langBtnActive : ''}`}
                      onClick={() => setQuestionLang('tr')}
                    >
                      TR
                    </button>
                    <button
                      type="button"
                      className={`${styles.langBtn} ${questionLang === 'en' ? styles.langBtnActive : ''}`}
                      onClick={() => setQuestionLang('en')}
                    >
                      EN
                    </button>
                  </div>
                </div>

                <p className={styles.questionText}>
                  {getTranslatedQuestion(question.question, questionLang)}
                </p>

                {questionLang === 'tr' ? (
                  <p className={styles.questionTip}>
                    💡 İpucu: Cevabınızı Türkçe yazabilirsiniz. İlgili teknik kavramları (örneğin <code>additive</code>, <code>single</code>, <code>async</code> vb.) orijinal teknik adlarıyla kullanmanız değerlendirmeyi olumlu etkiler.
                  </p>
                ) : (
                  <p className={styles.questionTip}>
                    💡 Tip: You can write your answer in English. Using core technical terms (e.g. <code>additive</code>, <code>single</code>, <code>async</code>, etc.) will improve evaluation accuracy.
                  </p>
                )}
              </div>

              <div className={styles.answerWrap}>
                <label className={styles.answerLabel}>
                  {locale === 'tr' ? 'Cevabınız' : 'Your Answer'}
                </label>
                <textarea
                  className={styles.textarea}
                  rows={5}
                  placeholder={
                    locale === 'tr'
                      ? 'Teknik bilginizi, uyguladığınız yaklaşımları veya kod mantığınızı açıklayın...'
                      : 'Explain your technical approach, implementation details, or code reasoning...'
                  }
                  value={answer}
                  onChange={e => setAnswer(e.target.value)}
                  disabled={submitting}
                  autoFocus
                />
              </div>
            </>
          )}

          {/* Evaluation Result State */}
          {!loading && evaluation && (
            <div className={styles.resultCard}>
              <div className={styles.resultOutcomeRow}>
                {evaluation.verdict === 'correct' && (
                  <span className="badge tier-ready">
                    ✓ {locale === 'tr' ? 'Doğrulandı · Başarılı' : 'Verified · Correct'}
                  </span>
                )}
                {evaluation.verdict === 'partial' && (
                  <span className="badge tier-developing">
                    ⚠ {locale === 'tr' ? 'Kısmen Doğru' : 'Partially Correct'}
                  </span>
                )}
                {evaluation.verdict === 'incorrect' && (
                  <span className="badge tier-not_ready">
                    ✕ {locale === 'tr' ? 'Henüz Yetersiz' : 'Not Sufficient'}
                  </span>
                )}
              </div>

              {evaluation.feedback && (
                <p className={styles.resultFeedback}>{evaluation.feedback}</p>
              )}

              {scoreDelta && scoreDelta.updated > scoreDelta.prev && (
                <div className={styles.scoreDelta}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <polyline points="18 15 12 9 6 15" />
                  </svg>
                  <span>
                    {locale === 'tr' ? 'Hazırlık Skoru Güncellendi:' : 'Readiness Score Updated:'}{' '}
                    %{scoreDelta.prev} ➔ %{scoreDelta.updated} (+%{scoreDelta.updated - scoreDelta.prev})
                  </span>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className={styles.footer}>
          {!evaluation ? (
            <>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={onClose}
                disabled={submitting}
              >
                {locale === 'tr' ? 'İptal' : 'Cancel'}
              </button>
              <button
                type="button"
                className="btn btn-primary"
                onClick={handleSubmit}
                disabled={!answer.trim() || submitting || !question}
              >
                {submitting ? (
                  <>
                    <span className="spinner" />
                    {locale === 'tr' ? 'Değerlendiriliyor...' : 'Evaluating...'}
                  </>
                ) : (
                  locale === 'tr' ? 'Cevabı Gönder' : 'Submit Answer'
                )}
              </button>
            </>
          ) : (
            <button
              type="button"
              className="btn btn-primary"
              onClick={handleFinish}
            >
              {locale === 'tr' ? 'Analize Dön' : 'Return to Analysis'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
