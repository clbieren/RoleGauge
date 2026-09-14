'use client';

import React, { useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import styles from './AuthModal.module.css';

interface AuthModalProps {
  locale?: 'tr' | 'en';
}

export default function AuthModal({ locale = 'tr' }: AuthModalProps) {
  const { isAuthModalOpen, authModalMode, openAuthModal, closeAuthModal, login, register } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  if (!isAuthModalOpen) return null;

  const isLogin = authModalMode === 'login';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!email.trim() || !password.trim()) {
      setError(locale === 'tr' ? 'Lütfen e-posta ve şifrenizi girin.' : 'Please enter email and password.');
      return;
    }

    if (!isLogin && password.length < 8) {
      setError(locale === 'tr' ? 'Şifre en az 8 karakter olmalıdır.' : 'Password must be at least 8 characters.');
      return;
    }

    setLoading(true);
    try {
      if (isLogin) {
        await login({ email: email.trim(), password });
      } else {
        await register({ email: email.trim(), password, full_name: fullName.trim() || undefined });
      }
      // Reset fields on success
      setEmail('');
      setPassword('');
      setFullName('');
    } catch (err) {
      setError(err instanceof Error ? err.message : (locale === 'tr' ? 'İşlem başarısız oldu.' : 'Operation failed.'));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.overlay} onClick={closeAuthModal}>
      <div className={styles.modal} onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className={styles.header}>
          <div className={styles.title}>
            <span>◈</span>
            <span>SkillLens</span>
          </div>
          <button
            type="button"
            className={styles.closeBtn}
            onClick={closeAuthModal}
            aria-label={locale === 'tr' ? 'Kapat' : 'Close'}
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>

        {/* Tabs */}
        <div className={styles.tabs}>
          <button
            type="button"
            className={`${styles.tab} ${isLogin ? styles.tabActive : ''}`}
            onClick={() => {
              setError('');
              openAuthModal('login');
            }}
          >
            {locale === 'tr' ? 'Giriş Yap' : 'Sign In'}
          </button>
          <button
            type="button"
            className={`${styles.tab} ${!isLogin ? styles.tabActive : ''}`}
            onClick={() => {
              setError('');
              openAuthModal('register');
            }}
          >
            {locale === 'tr' ? 'Kayıt Ol' : 'Create Account'}
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className={styles.body}>
          {error && <div className={styles.errorBox}>{error}</div>}

          {!isLogin && (
            <div className={styles.field}>
              <label className={styles.label}>
                {locale === 'tr' ? 'Ad Soyad (Opsiyonel)' : 'Full Name (Optional)'}
              </label>
              <input
                type="text"
                className={styles.input}
                placeholder={locale === 'tr' ? 'Örn: Ahmet Yılmaz' : 'e.g. Jane Doe'}
                value={fullName}
                onChange={e => setFullName(e.target.value)}
                autoComplete="name"
              />
            </div>
          )}

          <div className={styles.field}>
            <label className={styles.label}>
              {locale === 'tr' ? 'E-posta Adresi' : 'Email Address'}
            </label>
            <input
              type="email"
              className={styles.input}
              placeholder="developer@example.com"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
              autoComplete="email"
              autoFocus
            />
          </div>

          <div className={styles.field}>
            <label className={styles.label}>
              {locale === 'tr' ? 'Şifre' : 'Password'}
            </label>
            <input
              type="password"
              className={styles.input}
              placeholder={isLogin ? '••••••••' : (locale === 'tr' ? 'En az 8 karakter' : 'Min 8 characters')}
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
              autoComplete={isLogin ? 'current-password' : 'new-password'}
            />
          </div>

          <button type="submit" className={styles.submitBtn} disabled={loading}>
            {loading ? (
              <>
                <span className="spinner" style={{ width: 16, height: 16 }} />
                <span>{locale === 'tr' ? 'İşleniyor...' : 'Processing...'}</span>
              </>
            ) : isLogin ? (
              locale === 'tr' ? 'Giriş Yap' : 'Sign In'
            ) : (
              locale === 'tr' ? 'Hesap Oluştur' : 'Register'
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
