/**
 * API Client for RoleGauge Backend.
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface SubskillEvidence {
  composite_key: string;
  subskill_name: string;
  confidence: number;
  status: 'evidence_found' | 'not_yet_evidenced';
  evidence_sources: string[];
}

export interface SkillScore {
  skill_id: string;
  skill_name: string;
  score: number;
  importance: number;
  subskills: SubskillEvidence[];
}

export interface RepoInfo {
  repo_name: string;
  repo_url: string;
  description: string | null;
  primary_language: string | null;
  languages: Record<string, number>;
  stars: number;
  forks: number;
  topics: string[];
  is_relevant: boolean;
  relevant_files_count: number;
  evidence_found: string[];
}

export interface AnalyzeResponse {
  id: string;
  github_username: string;
  role_id: string;
  role_name: string;
  level: string;
  readiness_score: number;
  readiness_tier: string;
  readiness_label: string;
  total_repos_scanned: number;
  relevant_repos_found: number;
  skills: SkillScore[];
  repos: RepoInfo[];
  created_at: string;
}

export interface RoleInfo {
  role_id: string;
  title: string;
  description: string;
  category: string;
  levels: string[];
  skill_count: number;
}

export interface AnalyzeRequest {
  github_username: string;
  role_id: string;
  level: string;
  github_token?: string;
  use_ai?: boolean;
}

export async function analyzeProfile(request: AnalyzeRequest): Promise<AnalyzeResponse> {
  const res = await fetch(`${API_BASE}/api/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Analysis failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }

  return res.json();
}

export async function fetchRoles(): Promise<RoleInfo[]> {
  const res = await fetch(`${API_BASE}/api/roles`);
  if (!res.ok) throw new Error('Failed to fetch roles');
  const data = await res.json();
  return data.roles;
}

export async function fetchResult(id: string): Promise<AnalyzeResponse> {
  const res = await fetch(`${API_BASE}/api/results/${id}`);
  if (!res.ok) throw new Error('Result not found');
  return res.json();
}

export async function healthCheck(): Promise<{ status: string; roles_loaded: number }> {
  const res = await fetch(`${API_BASE}/api/health`);
  if (!res.ok) throw new Error('Backend unavailable');
  return res.json();
}
