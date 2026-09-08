/**
 * API Client for RoleGauge Backend.
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface SubskillEvidence {
  composite_key: string;
  subskill_name: string;
  confidence: number;
  status: 'evidence_found' | 'claimed' | 'not_yet_evidenced' | 'verified_gap';
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

/** Backend kapalıyken kullanılan fallback rol listesi */
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
];

export async function fetchRoles(): Promise<RoleInfo[]> {
  try {
    const res = await fetch(`${API_BASE}/api/roles`, { signal: AbortSignal.timeout(5000) });
    if (!res.ok) return FALLBACK_ROLES;
    const data = await res.json();
    // Backend { roles: [...] } veya direkt [...] döndürebilir
    const list: RoleInfo[] = Array.isArray(data) ? data : (data.roles ?? []);
    return list.length > 0 ? list : FALLBACK_ROLES;
  } catch {
    return FALLBACK_ROLES;
  }
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

export interface AssessmentQuestion {
  composite_key: string;
  subskill_name: string;
  question: string;
  type: string;
  level: string;
}

export interface AssessmentStartResponse {
  assessment_session_id: string;
  analysis_id: string;
  role_id: string;
  level: string;
  total_questions: number;
  questions: AssessmentQuestion[];
}

export interface AssessmentQuestionEvaluation {
  composite_key: string;
  subskill_name: string;
  user_answer: string;
  result: 'correct' | 'partially_correct' | 'incorrect';
  confidence_awarded: number;
  matched_keywords: string[];
  feedback: string;
}

export interface AssessmentSubmitResponse {
  assessment_session_id: string;
  analysis_id: string;
  evaluation_results: AssessmentQuestionEvaluation[];
  previous_score: number;
  updated_score: number;
  updated_tier: string;
  score_improved: boolean;
  updated_analysis?: AnalyzeResponse;
}

export async function startAssessment(
  analysisId: string,
  voluntaryCompositeKey: string
): Promise<AssessmentStartResponse> {
  const res = await fetch(`${API_BASE}/api/assessment/start`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
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
  answers: Record<string, string>
): Promise<AssessmentSubmitResponse> {
  const res = await fetch(`${API_BASE}/api/assessment/submit`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
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

