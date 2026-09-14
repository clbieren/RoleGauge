/**
 * useLocale hook — bileşenlerin locale değişikliğini dinlemesi için.
 */
'use client';

import { useState, useEffect, useCallback } from 'react';
import { Locale, getLocale, setLocale, initLocale, t, TranslationKey } from './i18n';

export function useLocale() {
  const [locale, setLocaleState] = useState<Locale>(() => {
    if (typeof window !== 'undefined') {
      initLocale();
      return getLocale();
    }
    return 'tr';
  });

  useEffect(() => {
    const handler = (e: Event) => {
      setLocaleState((e as CustomEvent<Locale>).detail);
    };
    window.addEventListener('locale-change', handler);
    return () => window.removeEventListener('locale-change', handler);
  }, []);

  const toggle = useCallback(() => {
    const next: Locale = locale === 'tr' ? 'en' : 'tr';
    setLocale(next);
    setLocaleState(next);
  }, [locale]);

  const translate = useCallback((key: TranslationKey) => t(key), [locale]); // eslint-disable-line react-hooks/exhaustive-deps

  return { locale, toggle, t: translate };
}
