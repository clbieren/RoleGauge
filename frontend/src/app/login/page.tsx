'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import styles from '@/components/AuthModal.module.css';

export default function LoginPage() {
  const router = useRouter();
  const { login, isAuthenticated } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // If already authenticated, redirect
  React.useEffect(() => {
    if (isAuthenticated) {
      router.push('/');
    }
  }, [isAuthenticated, router]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!email.trim() || !password.trim()) {
      setError('Lütfen e-posta ve şifrenizi girin.');
      return;
    }

    setLoading(true);
    try {
      await login({ email: email.trim(), password });
      router.push('/');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Giriş yapılamadı.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 20,
      background: 'radial-gradient(ellipse at 50% 20%, rgba(59, 130, 246, 0.08), transparent 70%), var(--bg-base)',
    }}>
      <div className={styles.modal} style={{ margin: 'auto' }}>
        <div className={styles.header}>
          <Link href="/" className={styles.title} style={{ textDecoration: 'none' }}>
            <span>◈</span>
            <span>SkillLens</span>
          </Link>
          <Link href="/" style={{ color: 'var(--text-muted)', fontSize: '0.85rem', textDecoration: 'none' }}>
            ← Ana Sayfa
          </Link>
        </div>

        <div className={styles.tabs}>
          <button type="button" className={`${styles.tab} ${styles.tabActive}`}>
            Giriş Yap
          </button>
          <Link href="/register" className={styles.tab} style={{ textDecoration: 'none', textAlign: 'center' }}>
            Kayıt Ol
          </Link>
        </div>

        <form onSubmit={handleSubmit} className={styles.body}>
          {error && <div className={styles.errorBox}>{error}</div>}

          <div className={styles.field}>
            <label className={styles.label}>E-posta Adresi</label>
            <input
              type="email"
              className={styles.input}
              placeholder="developer@example.com"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
              autoFocus
            />
          </div>

          <div className={styles.field}>
            <label className={styles.label}>Şifre</label>
            <input
              type="password"
              className={styles.input}
              placeholder="••••••••"
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="submit" className={styles.submitBtn} disabled={loading}>
            {loading ? (
              <>
                <span className="spinner" style={{ width: 16, height: 16 }} />
                <span>Giriş Yapılıyor...</span>
              </>
            ) : (
              'Giriş Yap'
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
