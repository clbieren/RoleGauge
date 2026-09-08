/**
 * SkillLens — Beceri ve Alt Beceri Türkçe Çevirileri
 * Basit ve genel kelimeleri (örn: Sahne, Animasyon, Fizik, Bellek, Yönetim) Türkçeleştirir;
 * sektörde yerleşmiş kalıpları (örn: Level Design, Shader, State Machine, Raycast) korur.
 */

const SKILL_MAP: Record<string, string> = {
  // Game Dev Skills
  "Game Engine Proficiency": "Oyun Motoru Yetkinliği",
  "Game Programming Languages": "Oyun Programlama Dilleri",
  "Game Mathematics": "Oyun Matematiği",
  "Game Design Fundamentals": "Oyun Tasarımı Temelleri",
  "Version Control for Games": "Versiyon Kontrolü (Git)",
  "Game AI & Behavior Systems": "Oyun Yapay Zekası & Davranış Sistemleri",
  "Performance Optimization & Profiling": "Performans Optimizasyonu & Profiling",
  "Shader & Graphics Programming": "Shader & Grafik Programlama",
  "Multiplayer & Networking": "Çok Oyunculu & Ağ Programlama",

  // Backend / Web / General Skills
  "API Design": "API Tasarımı",
  "Database Architecture": "Veritabanı Mimarisi",
  "Databases": "Veritabanları",
  "Authentication & Security": "Kimlik Doğrulama & Güvenlik",
  "Authentication & Authorization": "Kimlik Doğrulama & Yetkilendirme",
  "Caching & Performance": "Önbellekleme (Caching) & Performans",
  "Testing & Quality Assurance": "Test & Kalite Güvencesi",
  "Cloud Infrastructure": "Bulut Altyapısı",
  "Cloud Services": "Bulut Servisleri",
  "DevOps & CI/CD": "DevOps & CI/CD",
  "Containerization & Orchestration": "Konteynerleştirme (Docker/K8s)",
  "Frontend Architecture": "Frontend Mimarisi",
  "State Management": "State (Durum) Yönetimi",
  "Responsive Design & CSS": "Responsive Tasarım & CSS",
  "Web Performance": "Web Performansı",
  "Data Pipelines": "Veri Hatları (Pipelines)",
  "Data Modeling": "Veri Modelleme",
  "Machine Learning Operations": "Makine Öğrenimi Operasyonları (MLOps)",
  "Mobile Architecture": "Mobil Uygulama Mimarisi",
  "System Architecture": "Sistem Mimarisi",
  "Version Control & Collaboration": "Versiyon Kontrolü & Ekip Çalışması",
};

const SUBSKILL_MAP: Record<string, string> = {
  // Game Engine & General
  "Scene & Level Management": "Sahne & Level Yönetimi",
  "Physics System Usage": "Fizik Sistemi Kullanımı",
  "Animation & State Machines": "Animasyon & State Makineleri",
  "Particle & VFX Systems": "Parçacık & VFX Sistemleri",
  "Lighting & Rendering": "Aydınlatma & Rendering",
  "Lighting & Post-Processing": "Aydınlatma & Post-Processing",
  "Audio Integration": "Ses (Audio) Entegrasyonu",
  "UI & Canvas Systems": "Arayüz (UI) & Canvas Sistemleri",
  "Custom Editor Tools": "Özel Editör Araçları",
  "Asset Pipeline & Optimization": "Asset Yönetimi & Optimizasyon",
  "Input System Handling": "Input (Girdi) Sistemi",
  "Platform Abstraction & Porting": "Platform Uyumluluğu & Porting",

  // Programming & Architecture
  "Core Syntax": "Temel Sözdizimi (Syntax)",
  "Core Language Syntax": "Temel Dil Sözdizimi",
  "OOP & Design Patterns": "OOP & Tasarım Desenleri",
  "Memory Management": "Bellek Yönetimi (Memory)",
  "Data Structures & Algorithms": "Veri Yapıları & Algoritmalar",
  "ECS Architecture": "ECS Mimarisi (Entity Component System)",
  "Custom Memory Allocators": "Özel Bellek Dağıtıcıları (Allocators)",
  "Multithreading & Concurrency": "Çoklu İş Parçacığı (Multithreading)",
  "Asynchronous Programming": "Asenkron Programlama",

  // Math & Physics
  "Vector Operations": "Vektör İşlemleri",
  "Vector Mathematics": "Vektör Matematiği",
  "Quaternion & Rotations": "Quaternion & Rotasyonlar",
  "Matrices & Transforms": "Matrisler & Dönüşümler (Transforms)",
  "Trigonometry & Angles": "Trigonometri & Açılar",
  "Curves & Interpolation": "Eğriler & İnterpolasyon (Lerp/Slerp)",
  "Spatial Partitioning": "Uzamsal Bölümleme (Spatial Partitioning)",
  "Collision Detection": "Çarpışma Tespiti (Collision Detection)",

  // Game Design & AI
  "Core Mechanics Design": "Temel Mekanik Tasarımı",
  "Level Design Fundamentals": "Level Design Temelleri",
  "Balancing & Pacing": "Dengeleme (Balancing) & Oyun Ritmi",
  "Finite State Machines": "Sonlu Durum Makineleri (FSM)",
  "Pathfinding & Navigation": "Yol Bulma (Pathfinding) & Navigasyon",
  "Behavior Trees": "Davranış Ağaçları (Behavior Trees)",
  "Steering Behaviors": "Yönelme Davranışları (Steering Behaviors)",

  // Graphics & Performance
  "Shader Fundamentals": "Shader Temelleri",
  "Material Systems": "Materyal Sistemleri",
  "Post-Processing Effects": "Post-Processing Efektleri",
  "Frame Rate Optimization": "FPS & Kare Hızı Optimizasyonu",
  "Draw Call Reduction": "Draw Call Azaltma & Optimizasyon",
  "Memory Profiling & GC": "Bellek Profiling & GC Yönetimi",

  // Multiplayer
  "Client-Server Architecture": "Client-Server Mimarisi",
  "State Synchronization": "Durum Senkronizasyonu (State Sync)",
  "Lag Compensation & Prediction": "Lag Kompansasyonu & Tahmin",
  "Matchmaking & Lobbies": "Eşleştirme (Matchmaking) & Lobiler",

  // Web & Backend Subskills
  "RESTful Principles": "RESTful İlkeleri",
  "Request Validation & Error Handling": "İstek Doğrulama & Hata Yönetimi",
  "API Pagination & Filtering": "Sayfalama (Pagination) & Filtreleme",
  "Relational Schema Design": "İlişkisel Şema Tasarımı",
  "Database Indexing & Query Optimization": "İndeksleme & Sorgu Optimizasyonu",
  "Database Migrations": "Veritabanı Migrasyonları",
  "Unit Testing": "Birim Testleri (Unit Testing)",
  "Integration Testing": "Entegrasyon Testleri",
};

/**
 * Ana beceri adını aktif dile göre çevirir.
 */
export function tSkillName(name: string, locale: string = 'tr'): string {
  if (locale !== 'tr' || !name) return name;
  if (SKILL_MAP[name]) return SKILL_MAP[name];

  // Regex tabanlı akıllı dönüştürücü (kalıpları bozmadan)
  let translated = name;
  translated = translated.replace(/\bProficiency\b/gi, 'Yetkinliği');
  translated = translated.replace(/\bFundamentals\b/gi, 'Temelleri');
  translated = translated.replace(/\bManagement\b/gi, 'Yönetimi');
  translated = translated.replace(/\bArchitecture\b/gi, 'Mimarisi');
  translated = translated.replace(/\bDevelopment\b/gi, 'Geliştirme');
  translated = translated.replace(/\bLanguages\b/gi, 'Dilleri');
  translated = translated.replace(/\bMathematics\b/gi, 'Matematiği');
  translated = translated.replace(/\bSystems\b/gi, 'Sistemleri');
  translated = translated.replace(/\bOptimization\b/gi, 'Optimizasyonu');
  translated = translated.replace(/\bProgramming\b/gi, 'Programlama');
  return translated;
}

/**
 * Alt beceri adını aktif dile göre çevirir.
 */
export function tSubskillName(name: string, locale: string = 'tr'): string {
  if (locale !== 'tr' || !name) return name;
  if (SUBSKILL_MAP[name]) return SUBSKILL_MAP[name];

  let translated = name;
  // Basit isimler Türkçe olur, "level design" veya "state machine" gibi terimler korunur
  translated = translated.replace(/\bScene\b/gi, 'Sahne');
  translated = translated.replace(/\bAnimation\b/gi, 'Animasyon');
  translated = translated.replace(/\bPhysics\b/gi, 'Fizik');
  translated = translated.replace(/\bUsage\b/gi, 'Kullanımı');
  translated = translated.replace(/\bManagement\b/gi, 'Yönetimi');
  translated = translated.replace(/\bHandling\b/gi, 'Yönetimi');
  translated = translated.replace(/\bIntegration\b/gi, 'Entegrasyonu');
  translated = translated.replace(/\bSystems\b/gi, 'Sistemleri');
  translated = translated.replace(/\bFundamentals\b/gi, 'Temelleri');
  translated = translated.replace(/\bOperations\b/gi, 'İşlemleri');
  translated = translated.replace(/\bStructures\b/gi, 'Yapıları');
  translated = translated.replace(/\bDetection\b/gi, 'Tespiti');
  return translated;
}
