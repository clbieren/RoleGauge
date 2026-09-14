'use client';

import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import {
  UserResponse,
  UserLoginRequest,
  UserRegisterRequest,
  loginUser,
  registerUser,
  refreshAccessToken,
  getCurrentUser,
  getStoredToken,
  setStoredTokens,
  clearStoredTokens,
} from '@/lib/api';

interface AuthContextType {
  user: UserResponse | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (req: UserLoginRequest) => Promise<void>;
  register: (req: UserRegisterRequest) => Promise<void>;
  logout: () => void;
  isAuthModalOpen: boolean;
  authModalMode: 'login' | 'register';
  openAuthModal: (mode?: 'login' | 'register') => void;
  closeAuthModal: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<UserResponse | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  const [authModalMode, setAuthModalMode] = useState<'login' | 'register'>('login');

  // Hydrate user from stored tokens on mount
  useEffect(() => {
    let isMounted = true;

    async function hydrate() {
      const storedToken = getStoredToken();
      if (!storedToken) {
        if (isMounted) setIsLoading(false);
        return;
      }

      setToken(storedToken);

      try {
        const profile = await getCurrentUser(storedToken);
        if (isMounted) {
          setUser(profile);
        }
      } catch {
        // Token might be expired, attempt refresh
        try {
          const refreshToken = localStorage.getItem('rolegauge_refresh_token');
          if (refreshToken) {
            const refreshRes = await refreshAccessToken(refreshToken);
            setStoredTokens(refreshRes.access_token, refreshToken);
            if (isMounted) {
              setToken(refreshRes.access_token);
              const profile = await getCurrentUser(refreshRes.access_token);
              setUser(profile);
            }
          } else {
            clearStoredTokens();
            if (isMounted) {
              setToken(null);
              setUser(null);
            }
          }
        } catch {
          clearStoredTokens();
          if (isMounted) {
            setToken(null);
            setUser(null);
          }
        }
      } finally {
        if (isMounted) setIsLoading(false);
      }
    }

    hydrate();

    return () => {
      isMounted = false;
    };
  }, []);

  const login = useCallback(async (req: UserLoginRequest) => {
    setIsLoading(true);
    try {
      const res = await loginUser(req);
      setStoredTokens(res.access_token, res.refresh_token);
      setToken(res.access_token);
      setUser(res.user);
      setIsAuthModalOpen(false);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const register = useCallback(async (req: UserRegisterRequest) => {
    setIsLoading(true);
    try {
      const res = await registerUser(req);
      setStoredTokens(res.access_token, res.refresh_token);
      setToken(res.access_token);
      setUser(res.user);
      setIsAuthModalOpen(false);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const logout = useCallback(() => {
    clearStoredTokens();
    setToken(null);
    setUser(null);
  }, []);

  const openAuthModal = useCallback((mode: 'login' | 'register' = 'login') => {
    setAuthModalMode(mode);
    setIsAuthModalOpen(true);
  }, []);

  const closeAuthModal = useCallback(() => {
    setIsAuthModalOpen(false);
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!user,
        isLoading,
        login,
        register,
        logout,
        isAuthModalOpen,
        authModalMode,
        openAuthModal,
        closeAuthModal,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return ctx;
}
