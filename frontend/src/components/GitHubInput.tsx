'use client';

import { useState } from 'react';
import styles from './GitHubInput.module.css';

interface GitHubInputProps {
  value: string;
  onChange: (value: string) => void;
  token: string;
  onTokenChange: (value: string) => void;
}

export default function GitHubInput({ value, onChange, token, onTokenChange }: GitHubInputProps) {
  const [showToken, setShowToken] = useState(false);

  return (
    <div className={styles.container}>
      <div className={styles.inputWrapper}>
        <div className={styles.inputIcon}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
          </svg>
        </div>
        <input
          type="text"
          className={`input ${styles.mainInput}`}
          placeholder="GitHub kullanıcı adı veya profil URL'si"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          id="github-username-input"
          autoComplete="off"
          spellCheck={false}
        />
      </div>

      <button
        className={styles.tokenToggle}
        onClick={() => setShowToken(!showToken)}
        type="button"
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
        </svg>
        {showToken ? 'Token gizle' : 'GitHub Token (opsiyonel — daha yüksek rate limit)'}
        <svg
          width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"
          style={{ transform: showToken ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}
        >
          <polyline points="6 9 12 15 18 9"/>
        </svg>
      </button>

      {showToken && (
        <div className={styles.tokenField}>
          <input
            type="password"
            className="input"
            placeholder="ghp_xxxxxxxxxxxxxxxxxxxx"
            value={token}
            onChange={(e) => onTokenChange(e.target.value)}
            id="github-token-input"
            autoComplete="off"
          />
          <p className={styles.tokenHint}>
            Token olmadan rate limit: 60 req/saat. Token ile: 5000 req/saat.
          </p>
        </div>
      )}
    </div>
  );
}
