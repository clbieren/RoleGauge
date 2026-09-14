/**
 * API Client for RoleGauge Backend.
 * Strictly aligned with API_CONTRACT.md (v1.2.0).
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// ──────────────────────────────────────────────
// Contract Types (API_CONTRACT.md Section 4)
// ──────────────────────────────────────────────

export type SeniorityLevel = 'junior' | 'mid' | 'senior';

export type ReadinessTier = 'not_ready' | 'developing' | 'approaching' | 'ready' | 'exceeds';

export type EvidenceStatus = 'evidence_found' | 'claimed' | 'not_yet_evidenced' | 'verified_gap';

export interface ContributingSource {
  source: string;
  strength: number;
  signal: string;
  file_path?: string;
}

export interface SubskillEvidence {
  composite_key: string;       // e.g. "be_api_design.restful_principles"
  subskill_name: string;
  confidence: number;          // 0.0 to 1.0
  status: EvidenceStatus;
  evidence_sources: string[];
  contributing_sources?: ContributingSource[];
  ceiling_applied?: string;
  calculation_trace?: string;
}

export interface SkillScore {
  skill_id: string;
  skill_name: string;
  score: number;               // 0.0 to 1.0
  importance: number;          // 0.0 to 1.0
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

export interface AdPlacements {
  loading_screen: boolean;
  results_sidebar_left: boolean;
  results_sidebar_right: boolean;
}

export interface AnalyzeResponse {
  id: string;                  // UUID
  github_username: string;
  role_id: string;
  role_name: string;
  level: SeniorityLevel | string;
  readiness_score: number;     // 0.0 to 1.0
  readiness_tier: ReadinessTier | string;
  readiness_label: string;
  total_repos_scanned: number;
  relevant_repos_found: number;
  has_cv?: boolean;
  has_linkedin?: boolean;
  ai_enrichment_available?: boolean;
  analysis_tier?: string;
  ad_placements?: AdPlacements;
  skills: SkillScore[];
  repos: RepoInfo[];
  created_at: string;          // ISO 8601 UTC
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
  github_username?: string;
  role_id: string;
  level?: SeniorityLevel | string;
  github_token?: string;
  use_ai?: boolean;
}

export interface AssessmentQuestionPublic {
  composite_key: string;
  subskill_name: string;
  question: string;
  type: 'conceptual' | 'scenario' | 'practical_task' | string;
  level: SeniorityLevel | string;
}

export type AssessmentQuestion = AssessmentQuestionPublic;

export interface AssessmentStartResponse {
  assessment_session_id: string;
  analysis_id: string;
  role_id: string;
  level: SeniorityLevel | string;
  total_questions: number;
  questions: AssessmentQuestionPublic[];
}

export interface AssessmentQuestionEvaluation {
  composite_key: string;
  subskill_name: string;
  question?: string;
  type?: string;
  verdict: 'correct' | 'partial' | 'incorrect';
  status: 'evidence_found' | 'partial_answer' | 'verified_gap' | string;
  score: number;
  strength: number;
  match_ratio: number;
  matched_keywords_count: number;
  total_keywords_count: number;
  feedback: string;
}

export interface AssessmentSubmitResponse {
  assessment_session_id: string;
  analysis_id: string;
  evaluations: AssessmentQuestionEvaluation[];
  summary: {
    total: number;
    correct: number;
    partial: number;
    incorrect: number;
  };
  updated_analysis: AnalyzeResponse;
}

// ──────────────────────────────────────────────
// Auth & User Types
// ──────────────────────────────────────────────

export interface UserRegisterRequest {
  email: string;
  password: string;
  full_name?: string;
}

export interface UserLoginRequest {
  email: string;
  password: string;
}

export interface TokenRefreshRequest {
  refresh_token: string;
}

export interface UserResponse {
  id: string;
  email: string;
  full_name: string | null;
  is_active: boolean;
  created_at: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user: UserResponse;
}

export interface TokenRefreshResponse {
  access_token: string;
  token_type: string;
}

export interface UserAnalysisSummary {
  id: string;
  github_username: string;
  role_id: string;
  role_name: string;
  level: SeniorityLevel | string;
  readiness_score: number;
  readiness_tier: ReadinessTier | string;
  readiness_label: string;
  created_at: string;
}

// ──────────────────────────────────────────────
// CV & LinkedIn Upload Types
// ──────────────────────────────────────────────

export interface CVProjectData {
  name: string;
  description: string;
  skills_mentioned: string[];
}

export interface CVCertificateData {
  name: string;
  provider: string;
}

export interface CVParsedData {
  personal_info: Record<string, string>;
  education: Array<Record<string, string>>;
  experience: Array<Record<string, string>>;
  projects: CVProjectData[];
  skills: string[];
  certificates: CVCertificateData[];
  languages: string[];
  volunteering?: Array<Record<string, string>>;
  honors_awards?: Array<Record<string, string>>;
  publications?: Array<Record<string, string>>;
  recommendations?: Array<Record<string, string>>;
  detected_sections: string[];
}

export interface CVSkillMatch {
  composite_key: string;
  matched_from: string;
  matched_term: string;
  status: string;
  strength: number;
}

export interface CVCertificateMatch {
  certificate_name: string;
  classification: 'recognized_relevant' | 'recognized_no_mapping' | 'unrecognized_excluded';
  matched_composite_keys?: string[];
  score_contribution: number;
  matched_from_role?: string;
  category_group?: string;
}

export interface CVUploadResponse {
  parsed_cv: CVParsedData;
  skill_matches: CVSkillMatch[];
  certificate_matches: CVCertificateMatch[];
  scoring_preview: {
    readiness_score: number;
    readiness_tier: ReadinessTier | string;
    readiness_label: string;
    skills: SkillScore[];
  };
}

export interface LinkedInParsedData {
  personal_info: Record<string, string>;
  education: Array<Record<string, string>>;
  experience: Array<Record<string, string>>;
  projects: CVProjectData[];
  skills: string[];
  certificates: CVCertificateData[];
  languages: string[];
  volunteering?: Array<Record<string, string>>;
  honors_awards?: Array<Record<string, string>>;
  publications?: Array<Record<string, string>>;
  recommendations?: Array<{ recommender: string; text: string }>;
  detected_sections: string[];
}

export interface LinkedInSkillMatch {
  composite_key: string;
  matched_from: string;
  matched_term: string;
  status: string;
  strength: number;
}

export interface LinkedInCertificateMatch {
  certificate_name: string;
  classification: 'recognized_relevant' | 'recognized_no_mapping' | 'unrecognized_excluded';
  matched_composite_keys?: string[];
  score_contribution: number;
  matched_from_role?: string;
  category_group?: string;
}

export interface LinkedInUploadResponse {
  parsed_linkedin: LinkedInParsedData;
  skill_matches: LinkedInSkillMatch[];
  certificate_matches: LinkedInCertificateMatch[];
  scoring_preview: {
    readiness_score: number;
    readiness_tier: ReadinessTier | string;
    readiness_label: string;
    skills: SkillScore[];
  };
}

// ──────────────────────────────────────────────
// Token Helper (LocalStorage)
// ──────────────────────────────────────────────

export function getStoredToken(): string | null {
  if (typeof window === 'undefined') return null;
  try {
    return localStorage.getItem('rolegauge_access_token');
  } catch {
    return null;
  }
}

export function setStoredTokens(accessToken: string, refreshToken: string): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.setItem('rolegauge_access_token', accessToken);
    localStorage.setItem('rolegauge_refresh_token', refreshToken);
  } catch {
    // ignore
  }
}

export function clearStoredTokens(): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.removeItem('rolegauge_access_token');
    localStorage.removeItem('rolegauge_refresh_token');
    localStorage.removeItem('rolegauge_user');
  } catch {
    // ignore
  }
}

function buildHeaders(extraHeaders?: Record<string, string>, tokenOverride?: string): Record<string, string> {
  const headers: Record<string, string> = { ...extraHeaders };
  const token = tokenOverride !== undefined ? tokenOverride : getStoredToken();
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return headers;
}

// ──────────────────────────────────────────────
// API Functions
// ──────────────────────────────────────────────

/** POST /api/analyze — supports both JSON and Multipart FormData */
export async function analyzeProfile(
  request: AnalyzeRequest | FormData,
  token?: string
): Promise<AnalyzeResponse> {
  const isFormData = typeof FormData !== 'undefined' && request instanceof FormData;
  const headers = isFormData
    ? buildHeaders({}, token)
    : buildHeaders({ 'Content-Type': 'application/json' }, token);

  const res = await fetch(`${API_BASE}/api/analyze`, {
    method: 'POST',
    headers,
    body: isFormData ? request : JSON.stringify(request),
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Analysis failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }

  return res.json();
}

/** Fallback roles if backend is unreachable */
const FALLBACK_ROLES: RoleInfo[] = [
  { role_id: 'backend',          title: 'Backend Developer',      description: '', category: 'backend',          levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'frontend',         title: 'Frontend Developer',     description: '', category: 'frontend',         levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'fullstack',        title: 'Full Stack Developer',   description: '', category: 'fullstack',        levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'mobile',           title: 'Mobile Developer',       description: '', category: 'mobile',           levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'android',          title: 'Android Developer',      description: '', category: 'android',          levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'ios',              title: 'iOS Developer',          description: '', category: 'ios',              levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'devops',           title: 'DevOps Engineer',        description: '', category: 'devops',           levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'data-analyst',     title: 'Data Analyst',           description: '', category: 'data-analyst',     levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'data-engineer',    title: 'Data Engineer',          description: '', category: 'data-engineer',    levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'machine-learning', title: 'Machine Learning Engineer', description: '', category: 'machine-learning', levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'ai-engineer',      title: 'AI Engineer',            description: '', category: 'ai-engineer',      levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'mlops',            title: 'MLOps Engineer',         description: '', category: 'mlops',            levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'qa-engineer',      title: 'QA Engineer',            description: '', category: 'qa-engineer',      levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'cyber-security',   title: 'Cybersecurity Engineer', description: '', category: 'cyber-security',   levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'network-engineer', title: 'Network Engineer',       description: '', category: 'network-engineer', levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'game-dev',         title: 'Game Developer',         description: '', category: 'game-dev',         levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'blockchain',       title: 'Blockchain Developer',   description: '', category: 'blockchain',       levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'technical-writer', title: 'Technical Writer',       description: '', category: 'technical-writer', levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'api-design',       title: 'API Designer',           description: '', category: 'api-design',       levels: ['junior','mid','senior'], skill_count: 0 },
  { role_id: 'ux-design',        title: 'UX Designer',            description: '', category: 'ux-design',        levels: ['junior','mid','senior'], skill_count: 0 },
];

export async function fetchRoles(): Promise<RoleInfo[]> {
  try {
    const res = await fetch(`${API_BASE}/api/roles`, { signal: AbortSignal.timeout(5000) });
    if (!res.ok) return FALLBACK_ROLES;
    const data = await res.json();
    const list: RoleInfo[] = Array.isArray(data) ? data : (data.roles ?? []);
    return list.length > 0 ? list : FALLBACK_ROLES;
  } catch {
    return FALLBACK_ROLES;
  }
}

export async function fetchResult(id: string, token?: string): Promise<AnalyzeResponse> {
  const res = await fetch(`${API_BASE}/api/results/${id}`, {
    headers: buildHeaders({}, token),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Result not found' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function healthCheck(): Promise<{ status: string; roles_loaded: number; ai_provider: string }> {
  const res = await fetch(`${API_BASE}/api/health`);
  if (!res.ok) throw new Error('Backend unavailable');
  return res.json();
}

export async function startAssessment(
  analysisId: string,
  voluntaryCompositeKey: string,
  token?: string
): Promise<AssessmentStartResponse> {
  const res = await fetch(`${API_BASE}/api/assessment/start`, {
    method: 'POST',
    headers: buildHeaders({ 'Content-Type': 'application/json' }, token),
    body: JSON.stringify({
      analysis_id: analysisId,
      voluntary_composite_keys: [voluntaryCompositeKey],
      max_questions: 1,
    }),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Failed to start assessment' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function submitAssessment(
  sessionId: string,
  answers: Record<string, string>,
  token?: string
): Promise<AssessmentSubmitResponse> {
  const res = await fetch(`${API_BASE}/api/assessment/submit`, {
    method: 'POST',
    headers: buildHeaders({ 'Content-Type': 'application/json' }, token),
    body: JSON.stringify({
      assessment_session_id: sessionId,
      answers,
    }),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Failed to submit assessment' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

// ──────────────────────────────────────────────
// Auth API Endpoints
// ──────────────────────────────────────────────

export async function registerUser(req: UserRegisterRequest): Promise<TokenResponse> {
  const res = await fetch(`${API_BASE}/api/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(req),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Registration failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function loginUser(req: UserLoginRequest): Promise<TokenResponse> {
  const res = await fetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(req),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Login failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function refreshAccessToken(refreshToken: string): Promise<TokenRefreshResponse> {
  const res = await fetch(`${API_BASE}/api/auth/refresh`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh_token: refreshToken }),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Session refresh failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function getCurrentUser(token?: string): Promise<UserResponse> {
  const res = await fetch(`${API_BASE}/api/auth/me`, {
    headers: buildHeaders({}, token),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Unauthorized' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function getMyAnalyses(token?: string): Promise<UserAnalysisSummary[]> {
  const res = await fetch(`${API_BASE}/api/users/me/analyses`, {
    headers: buildHeaders({}, token),
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Failed to fetch analyses' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

// ──────────────────────────────────────────────
// Upload API Endpoints (CV & LinkedIn)
// ──────────────────────────────────────────────

export async function uploadCV(
  file: File,
  roleId: string,
  level: string = 'mid',
  token?: string
): Promise<CVUploadResponse> {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('role_id', roleId);
  formData.append('level', level);

  const res = await fetch(`${API_BASE}/api/cv/upload`, {
    method: 'POST',
    headers: buildHeaders({}, token),
    body: formData,
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'CV upload failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

export async function uploadLinkedIn(
  file: File,
  roleId: string,
  level: string = 'mid',
  token?: string
): Promise<LinkedInUploadResponse> {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('role_id', roleId);
  formData.append('level', level);

  const res = await fetch(`${API_BASE}/api/linkedin/upload`, {
    method: 'POST',
    headers: buildHeaders({}, token),
    body: formData,
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'LinkedIn upload failed' }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }
  return res.json();
}
