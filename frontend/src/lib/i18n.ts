/**
 * SkillLens — TR/EN Localization
 * Varsayılan dil Türkçe. Kullanıcı TR/EN arasında geçiş yapabilir.
 */

export type Locale = 'tr' | 'en';

const translations = {
  tr: {
    // Nav
    navHowItWorks: 'Nasıl çalışır?',
    navSignIn: 'Giriş yap',
    navDashboard: 'Panel',
    navAnalyses: 'Analizler',
    navAssessments: 'Değerlendirmeler',
    navSettings: 'Ayarlar',
    navNewAnalysis: 'Yeni analiz',
    navWhatWeAnalyze: 'Kapsam',
    navEvidence: 'Kod Kanıtları',
    navSampleAnalysis: 'Örnek Analiz',
    navTrust: 'Güvenilirlik',

    // Landing Hero
    heroBadge: 'Açık Kaynak Geliştirici Değerlendirme Platformu',
    heroTitle: 'Geliştirici profilini değerlendir',
    heroSubtitle: 'GitHub projelerinin hedeflediğin role beklenen becerilerle ne kadar örtüştüğünü gör.',
    heroQuickSample: 'Veya doğrudan örnek analizi görüntüle',
    formGithubLabel: 'GitHub kullanıcı adı',
    formGithubPlaceholder: 'kullanıcıadı',
    formRoleLabel: 'Hedef rol',
    formRolePlaceholder: 'Rol seç',
    formLevelLabel: 'Seviye',
    formLevelJunior: 'Junior',
    formLevelMid: 'Mid',
    formLevelSenior: 'Senior',
    formUploadLabel: 'CV veya LinkedIn çıktısı yükle',
    formUploadDesc: 'İsteğe bağlı · PDF / DOCX',
    formUploadDrag: 'Sürükleyip bırak veya göz at',
    formUploadComingSoon: 'Yakında',
    formAnalyzeBtn: 'Profili analiz et',
    formTokenToggle: 'GitHub Token (opsiyonel)',
    formTokenHint: 'Token olmadan rate limit: 60 istek/saat. Token ile: 5.000 istek/saat.',

    // Dashboard Preview (Hero Right - Multi-Demo Showcase)
    previewDemoBadge: 'Örnek Raporlar (Demo)',
    previewTabGame: '🎮 Game Dev',
    previewTabBackend: '⚙️ Backend',
    previewTabFrontend: '🎨 Frontend',
    previewFullReportBtn: 'Örnek analizi tam ekranda aç',
    previewRole: 'Backend Developer',
    previewLevel: 'Mid-Level',
    previewReadiness: 'Hazırlık Skoru',
    previewReady: 'Hazır',
    previewAnalyzedRepos: '3 repository · 42 dosya incelendi',
    previewSkillApi: 'API Tasarımı & HTTP Mimarisi',
    previewSkillDb: 'Veritabanı & ORM Modelleme',
    previewSkillAuth: 'Kimlik Doğrulama & Güvenlik',
    previewSkillTesting: 'Birim & Entegrasyon Testleri',
    previewEvidencedBadge: 'Doğrulandı',

    // Game Dev Demo
    previewGameRole: 'Game Developer',
    previewGameLevel: 'Mid-Level',
    previewGameRepos: '4 repository · 58 dosya incelendi',
    previewGameSkill1: 'Gameplay & State Mimarisi',
    previewGameSkill2: 'Matematik & Vektör Fiziği',
    previewGameSkill3: 'Shader & Rendering',
    previewGameSkill4: 'Level Design & Optimizasyon',
    previewGameProvenance: '58 dosya · Unity / C# AST tarandı',

    // Backend Demo
    previewBackendRole: 'Backend Engineer',
    previewBackendLevel: 'Senior',
    previewBackendRepos: '6 repository · 124 dosya incelendi',
    previewBackendSkill1: 'API Tasarımı & HTTP Mimarisi',
    previewBackendSkill2: 'Veritabanı & ORM Modelleme',
    previewBackendSkill3: 'Kimlik Doğrulama & Güvenlik',
    previewBackendSkill4: 'Birim & Entegrasyon Testleri',
    previewBackendProvenance: '124 dosya · Python / FastAPI AST tarandı',

    // Frontend Demo
    previewFrontendRole: 'Frontend Developer',
    previewFrontendLevel: 'Junior',
    previewFrontendRepos: '3 repository · 36 dosya incelendi',
    previewFrontendSkill1: 'Komponent Mimarisi & React',
    previewFrontendSkill2: 'TypeScript & Tip Güvenliği',
    previewFrontendSkill3: 'State Yönetimi & Veri Akışı',
    previewFrontendSkill4: 'CSS / Responsive & UI Pratikleri',
    previewFrontendProvenance: '36 dosya · React / TypeScript AST tarandı',

    // How it works
    howSectionTag: 'Süreç',
    howTitle: 'Nasıl çalışır?',
    howSubtitle: 'Üç adımda GitHub projelerinin hedef rolün yetkinlik standartlarıyla karşılaştırmasını al.',
    step1Number: '01',
    step1Title: 'GitHub Profilini Bağla',
    step1Desc: 'Kullanıcı adını girmen yeterli. Herkese açık repository\'lerin taranarak ilgili projeler filtrelenir.',
    step2Number: '02',
    step2Title: 'Kod ve Projelerin İncelensin',
    step2Desc: 'Repository dosyaları, kütüphaneler, mimari desenler ve test pratikleri rol beklentilerine göre incelenir.',
    step3Number: '03',
    step3Title: 'Rol Uyumluluğu ve Kanıtları Gör',
    step3Desc: 'Hangi becerilerin kodla kanıtlandığını, hangilerinin henüz gözlenmediğini ve somut dosya referanslarını incele.',

    // What We Analyze
    analyzeSectionTag: 'Kapsam',
    analyzeTitle: 'Neleri inceliyoruz?',
    analyzeSubtitle: 'Yalnızca commit sayısına veya repo yıldızlarına değil; kodun kalitesine, mimarisine ve mühendislik pratiklerine odaklanıyoruz.',
    analyzeCat1Title: 'Teknik Yetkinlikler',
    analyzeCat1Desc: 'Programlama dilleri, modern framework\'ler, API sözleşmeleri, veritabanı şemaları ve asenkron veri akışları.',
    analyzeCat1Item1: 'REST & GraphQL API Tasarımı',
    analyzeCat1Item2: 'Veritabanı Modelleme & Migration',
    analyzeCat1Item3: 'Tip Güvenliği & Asenkron Mimari',
    analyzeCat2Title: 'Geliştirme Pratikleri',
    analyzeCat2Desc: 'Kod organizasyonu, hata yönetimi stratejileri, birim ve entegrasyon testleri, CI/CD yapılandırmaları.',
    analyzeCat2Item1: 'Birim & Entegrasyon Testleri',
    analyzeCat2Item2: 'Temiz Kod & Katmanlı Mimari',
    analyzeCat2Item3: 'Ortam Değişkenleri & Konfigürasyon',
    analyzeCat3Title: 'Proje Deneyimi',
    analyzeCat3Desc: 'Gerçek dünya isterleri, ölçeklenebilirlik modelleri, servis entegrasyonları ve dokümantasyon kalitesi.',
    analyzeCat3Item1: 'Üretime Hazır Proje Mimarisi',
    analyzeCat3Item2: 'Yetkilendirme & Güvenlik Pratikleri',
    analyzeCat3Item3: 'Kapsamlı README & API Dokümantasyonu',

    // Evidence Section
    evidenceSectionTag: 'Şeffaflık',
    evidenceTitle: 'Somut kod kanıtlarına dayalı değerlendirme',
    evidenceSubtitle: 'Soyut puanlar yerine, her beceri için repository ve dosya düzeyinde doğrulanmış kanıtlar sunulur.',
    evidenceSnippetFile1: 'src/services/order_service.py:84',
    evidenceSnippetDesc1: 'FastAPI dependency injection & transactional session handling',
    evidenceSnippetFile2: 'src/security/jwt_handler.py:32',
    evidenceSnippetDesc2: 'RS256 JWT validation & refresh token rotation pattern',
    evidenceSnippetFile3: 'tests/integration/test_orders.py:45',
    evidenceSnippetDesc3: 'Pytest fixture mocking external payment gateway',
    evidenceStatusVerified: 'Doğrulandı',

    // Role Comparison
    compareSectionTag: 'Bağlamsal Analiz',
    compareTitle: 'Rol bazlı değerlendirme',
    compareSubtitle: 'Aynı GitHub profili, farklı rollerin gereksinimlerine göre tamamen farklı değerlendirilir. Genel bir "yazılımcı puanı" yoktur; hedef role uyum vardır.',
    compareRole1: 'Backend Developer',
    compareRole1Score: '%91',
    compareRole1Tier: 'Hazır',
    compareRole2: 'Frontend Developer',
    compareRole2Score: '%64',
    compareRole2Tier: 'Gelişiyor',
    compareRole3: 'DevOps / Cloud Engineer',
    compareRole3Score: '%42',
    compareRole3Tier: 'Hazır Değil',

    // Missing Skills & Gaps
    missingSectionTag: 'Gelişim Alanları',
    missingTitle: 'Eksikleri yapıcı bir dille tespit et',
    missingSubtitle: 'Henüz kodda yer almayan beceriler bir eksiklik olarak damgalanmaz, odaklanılması gereken gelişim fırsatları olarak gösterilir. Kodunuzda olmayan becerileri interaktif değerlendirmeyle kanıtlayabilirsiniz.',
    missingCardFoundTitle: 'Kodla Kanıtlanmış',
    missingCardFoundDesc: 'Herkese açık projelerinizde tespit edilen ve doğrulanan teknik yetkinlikler.',
    missingCardNotYetTitle: 'Henüz Kanıtlanmadı',
    missingCardNotYetDesc: 'Projelerinizde henüz doğrudan rastlanmayan ancak rol için beklenen alanlar.',
    missingInteractiveBadge: 'İnteraktif Kanıtlama',
    missingInteractiveDesc: '"Bu beceriyi kanıtla" butonuna tıklayarak pratik bir soru yanıtlayabilir ve skorunuzu anında güncelleyebilirsiniz.',

    // Sample Analysis Section
    sampleSectionTag: 'Canlı Demo',
    sampleTitle: 'Örnek bir analiz sonucunu incele',
    sampleSubtitle: 'Gerçek bir profil analizi yapmadan önce SkillLens\'in sağladığı ayrıntılı içgörüleri sentetik demo verisiyle keşfet.',
    sampleProfileUser: '@demo-developer',
    sampleProfileRole: 'Backend Developer · Mid-Level',
    sampleReadiness: '%78 Hazır',
    sampleRepos: '3 repository incelendi',
    sampleActionBtn: 'Örnek analizi görüntüle',
    sampleSyntheticTag: 'Sentetik Demo',
    demoBannerLabel: 'Demo Analiz · Sentetik demo verisidir, gerçek kullanıcı verisi değildir',

    // Personas Section
    personasSectionTag: 'Kullanıcı Profilleri',
    personasTitle: 'Kariyerinin her aşamasında netlik kazan',
    personasSubtitle: 'İster ilk işine hazırlanan bir Junior, ister Senior seviyeye geçmek isteyen bir Mid-level geliştirici ol.',
    persona1Title: 'Junior Geliştiriciler',
    persona1Desc: 'İlk iş başvurularından önce portfolyondaki somut eksikleri gör, iş ilanlarında aranan standartlara tam olarak hazırlan.',
    persona2Title: 'Mid-Level Geliştiriciler',
    persona2Desc: 'Bir sonraki kıdem seviyesine (Senior) geçiş için hangi mimari desenlerin ve test standartlarının profilinde eksik kaldığını keşfet.',
    persona3Title: 'Kariyer Değiştirenler & Alaylılar',
    persona3Desc: 'Geleneksel CS diploması yerine projelerinin ve kod yetkinliklerinin teknik doğruluğunu objektif verilerle kanıtla.',

    // Trust & Security Section
    trustSectionTag: 'Gizlilik & Güvenlik',
    trustTitle: 'Şeffaf ve güvenli analiz ilkeleri',
    trustSubtitle: 'Verilerinize ve kodunuza nasıl yaklaştığımız konusunda tamamen açığız.',
    trustPillar1Title: 'Salt Okunur Kamu Erişimi',
    trustPillar1Desc: 'Yalnızca GitHub üzerinde herkese açık (public) repository\'ler taranır. Gizli (private) depolarınıza erişim talebinde bulunulmaz.',
    trustPillar2Title: 'Sıfır Yazma İzni',
    trustPillar2Desc: 'Hesabınıza, depolarınıza veya commit geçmişinize hiçbir yazma ya da değişiklik izni istenmez.',
    trustPillar3Title: 'İsteğe Bağlı Token',
    trustPillar3Desc: 'GitHub Personal Access Token yalnızca API saatlik istek limitini yükseltmek içindir; oturumunuz sırasında geçici olarak kullanılır.',
    trustPillar4Title: 'Kapsamlı Kaynak Şeffaflığı',
    trustPillar4Desc: 'Değerlendirmeler yalnızca seçtiğiniz hedef role ve tespit edilen somut kod göstergelerine dayanır. CV/LinkedIn entegrasyonu geliştirme aşamasındadır.',

    // Final CTA & Footer
    ctaTitle: 'Hedeflediğin role ne kadar yakınsın?',
    ctaSubtitle: 'GitHub kullanıcı adını gir, birkaç saniye içinde rolüne özel beceri uyum raporunu incele.',
    ctaAnalyzeBtn: 'Hemen analiz et',
    ctaSampleBtn: 'Örnek analizi incele',
    footerTagline: 'Geliştirici rol yetkinliği ve kod kanıtı değerlendirme platformu.',
    footerRights: 'Tüm hakları saklıdır.',
    footerPrivacyNote: 'SkillLens, kamuya açık GitHub verilerini hedef rol standartlarına göre analiz eden bağımsız bir geliştirici aracıdır.',

    // Loading
    loadingTitle: 'Profil analiz ediliyor',
    loadingStep1: "GitHub'a bağlanılıyor",
    loadingStep2: "Repository'ler toplanıyor",
    loadingStep3: 'Projeler inceleniyor',
    loadingStep4: 'Beceriler değerlendiriliyor',
    loadingStep5: 'Sonuçlar hazırlanıyor',
    loadingRepositories: 'repository',
    loadingFiles: 'dosya',

    // Dashboard
    dashboardTitle: 'Analiz',
    dashboardAnalyzedOn: 'tarihinde analiz edildi',
    dashboardRepoCount: 'repository',
    dashboardFilesReviewed: 'dosya incelendi',
    dashboardRelevantRepos: 'ilgili repo',
    dashboardReadiness: 'Hazırlık',
    dashboardReadinessDesc: {
      not_ready: 'GitHub profili bu rol için beklenen becerilerin büyük çoğunluğunu henüz yansıtmıyor.',
      developing: 'Temel beceriler görünüyor ancak birçok kritik alan henüz doğrulanamadı.',
      approaching: 'Profil bu rol için iyi bir temel gösteriyor. Birkaç önemli alan daha geliştirilebilir.',
      ready: 'Hedef rol için beklenen becerilerin büyük çoğunluğu GitHub profilinde doğrulanmış görünüyor.',
      exceeds: 'Profil bu rol için beklenen seviyelerin üzerinde bir derinlik ve kapsam gösteriyor.',
    } as Record<string, string>,

    // Summary cards
    summaryRepositories: 'Repository',
    summarySkills: 'Beceri',
    summaryCoreSkills: 'Temel beceri',

    // Skills
    skillsOverviewTitle: 'Beceriler genel bakış',
    skillsBreakdownTitle: 'Beceri detayları',
    skillsEvidenced: 'kanıtlandı',

    // Evidence
    evidenceFound: 'Kanıt bulundu',
    evidenceClaimed: 'Kullanıcı beyanı',
    evidenceClaimedDesc: 'Kullanıcı bu beceriye sahip olduğunu belirtiyor ancak GitHub kodunda yeterli doğrulama bulunmuyor.',
    evidenceNotYet: 'Henüz kanıtlanmadı',
    evidenceNotYetDesc: "GitHub'da bu beceriye ilişkin yeterli kanıt bulunamadı.",
    evidenceSources: 'Kanıt kaynakları',
    evidenceMore: 'daha',
    evidenceProveSkill: 'Bu beceriyi kanıtla',

    // Repos
    reposTitle: 'Repository\'ler',
    repoStars: 'Yıldız',
    repoLanguages: 'Diller',
    repoRelevance: 'İlgi',
    repoRelevant: 'İlgili',
    repoNotRelevant: 'İlgili değil',
    repoFiles: 'dosya',
    repoViewOnGitHub: "GitHub'da görüntüle",
    repoEvidenceFound: 'Bulunan kanıtlar',
    repoRelevantFor: 'için ilgili',

    // Tiers
    tierNotReady: 'Hazır Değil',
    tierDeveloping: 'Gelişiyor',
    tierApproaching: 'Yaklaşıyor',
    tierReady: 'Hazır',
    tierExceeds: 'Üstünde',

    // Errors
    errorGeneral: 'Analiz başarısız',
    errorRetry: 'Tekrar dene',
    errorGithubNotFound: 'GitHub kullanıcısı bulunamadı.',
    errorRateLimit: 'İstek limiti aşıldı. Lütfen daha sonra tekrar deneyin.',
    errorTimeout: 'İstek zaman aşımına uğradı.',

    // Empty states
    emptyNoEvidence: 'Kanıt bulunamadı',
    emptyNoEvidenceDesc: 'Bu beceri analize dahil edilen repository\'lerden doğrulanamadı.',
    emptyNoRepos: 'İlgili repository bulunamadı',
    emptyNoReposDesc: 'Analiz edilen repository\'lerin hiçbiri bu rol için yeterli bilgi sağlamadı.',
    emptyAnalysisError: 'Analiz tamamlanamadı',

    // Assessment
    assessmentTitle: 'Değerlendirme',
    assessmentQuestion: 'Soru',
    assessmentOf: '/',
    assessmentSubmit: 'Cevabı gönder',
    assessmentContinue: 'Devam et',
    assessmentYourAnswer: 'Cevabınız',
    assessmentCorrect: 'Doğru',
    assessmentPartial: 'Kısmen doğru',
    assessmentIncorrect: 'Yanlış',

    // Misc
    loading: 'Yükleniyor...',
    optional: 'İsteğe bağlı',
  },
  en: {
    // Nav
    navHowItWorks: 'How it works',
    navSignIn: 'Sign in',
    navDashboard: 'Dashboard',
    navAnalyses: 'Analyses',
    navAssessments: 'Assessments',
    navSettings: 'Settings',
    navNewAnalysis: 'New analysis',
    navWhatWeAnalyze: 'Scope',
    navEvidence: 'Code Evidence',
    navSampleAnalysis: 'Sample Analysis',
    navTrust: 'Trust & Privacy',

    // Landing Hero
    heroBadge: 'Open Source Developer Assessment Platform',
    heroTitle: 'Assess your developer profile',
    heroSubtitle: 'See how your GitHub projects match the skills expected for your target role.',
    heroQuickSample: 'Or view the sample analysis directly',
    formGithubLabel: 'GitHub username',
    formGithubPlaceholder: 'username',
    formRoleLabel: 'Target role',
    formRolePlaceholder: 'Select role',
    formLevelLabel: 'Level',
    formLevelJunior: 'Junior',
    formLevelMid: 'Mid',
    formLevelSenior: 'Senior',
    formUploadLabel: 'Upload CV or LinkedIn export',
    formUploadDesc: 'Optional · PDF / DOCX',
    formUploadDrag: 'Drag and drop or browse',
    formUploadComingSoon: 'Coming soon',
    formAnalyzeBtn: 'Analyze profile',
    formTokenToggle: 'GitHub Token (optional)',
    formTokenHint: 'Without token: 60 req/hour. With token: 5,000 req/hour.',

    // Dashboard Preview (Hero Right - Multi-Demo Showcase)
    previewDemoBadge: 'Sample Reports (Demo)',
    previewTabGame: '🎮 Game Dev',
    previewTabBackend: '⚙️ Backend',
    previewTabFrontend: '🎨 Frontend',
    previewFullReportBtn: 'Open full sample report',
    previewRole: 'Backend Developer',
    previewLevel: 'Mid-Level',
    previewReadiness: 'Readiness Score',
    previewReady: 'Ready',
    previewAnalyzedRepos: '3 repositories · 42 files reviewed',
    previewSkillApi: 'API Design & HTTP Architecture',
    previewSkillDb: 'Database & ORM Modeling',
    previewSkillAuth: 'Authentication & Security',
    previewSkillTesting: 'Unit & Integration Testing',
    previewEvidencedBadge: 'Evidenced',

    // Game Dev Demo
    previewGameRole: 'Game Developer',
    previewGameLevel: 'Mid-Level',
    previewGameRepos: '4 repositories · 58 files reviewed',
    previewGameSkill1: 'Gameplay & State Architecture',
    previewGameSkill2: 'Math & Vector Physics',
    previewGameSkill3: 'Shader & Rendering',
    previewGameSkill4: 'Level Design & Optimization',
    previewGameProvenance: '58 files · Unity / C# AST scanned',

    // Backend Demo
    previewBackendRole: 'Backend Engineer',
    previewBackendLevel: 'Senior',
    previewBackendRepos: '6 repositories · 124 files reviewed',
    previewBackendSkill1: 'API Design & HTTP Architecture',
    previewBackendSkill2: 'Database & ORM Modeling',
    previewBackendSkill3: 'Authentication & Security',
    previewBackendSkill4: 'Unit & Integration Testing',
    previewBackendProvenance: '124 files · Python / FastAPI AST scanned',

    // Frontend Demo
    previewFrontendRole: 'Frontend Developer',
    previewFrontendLevel: 'Junior',
    previewFrontendRepos: '3 repositories · 36 files reviewed',
    previewFrontendSkill1: 'Component Architecture & React',
    previewFrontendSkill2: 'TypeScript & Type Safety',
    previewFrontendSkill3: 'State Management & Data Flow',
    previewFrontendSkill4: 'CSS / Responsive & UI Standards',
    previewFrontendProvenance: '36 files · React / TypeScript AST scanned',

    // How it works
    howSectionTag: 'Process',
    howTitle: 'How it works',
    howSubtitle: 'Compare your GitHub projects against target role expectations in three simple steps.',
    step1Number: '01',
    step1Title: 'Connect GitHub Profile',
    step1Desc: 'Simply enter your username. Your public repositories are scanned and relevant projects are identified.',
    step2Number: '02',
    step2Title: 'Codebase & Projects Analyzed',
    step2Desc: 'Source files, dependency manifests, architectural patterns, and testing practices are analyzed against role expectations.',
    step3Number: '03',
    step3Title: 'See Role Fit & Evidence',
    step3Desc: 'Review which skills are backed by code evidence, identify development gaps, and inspect concrete file references.',

    // What We Analyze
    analyzeSectionTag: 'Scope',
    analyzeTitle: 'What do we analyze?',
    analyzeSubtitle: 'We do not just count commits or stars; we focus on code quality, architecture, and real engineering practices.',
    analyzeCat1Title: 'Technical Skills',
    analyzeCat1Desc: 'Programming languages, modern frameworks, API contracts, database schemas, and asynchronous data pipelines.',
    analyzeCat1Item1: 'REST & GraphQL API Design',
    analyzeCat1Item2: 'Database Modeling & Migrations',
    analyzeCat1Item3: 'Type Safety & Async Architecture',
    analyzeCat2Title: 'Development Practices',
    analyzeCat2Desc: 'Code organization, robust error handling, unit and integration test coverage, and CI/CD pipelines.',
    analyzeCat2Item1: 'Unit & Integration Tests',
    analyzeCat2Item2: 'Clean Architecture & Patterns',
    analyzeCat2Item3: 'Configuration & Env Hygiene',
    analyzeCat3Title: 'Project Experience',
    analyzeCat3Desc: 'Real-world requirements, scalability patterns, external service integrations, and documentation standards.',
    analyzeCat3Item1: 'Production-Grade Architecture',
    analyzeCat3Item2: 'Authentication & Security Best Practices',
    analyzeCat3Item3: 'Comprehensive README & API Docs',

    // Evidence Section
    evidenceSectionTag: 'Transparency',
    evidenceTitle: 'Evidence-based evaluation grounded in real code',
    evidenceSubtitle: 'Instead of arbitrary scores, every skill is verified with concrete repository and file-level references.',
    evidenceSnippetFile1: 'src/services/order_service.py:84',
    evidenceSnippetDesc1: 'FastAPI dependency injection & transactional session handling',
    evidenceSnippetFile2: 'src/security/jwt_handler.py:32',
    evidenceSnippetDesc2: 'RS256 JWT validation & refresh token rotation pattern',
    evidenceSnippetFile3: 'tests/integration/test_orders.py:45',
    evidenceSnippetDesc3: 'Pytest fixture mocking external payment gateway',
    evidenceStatusVerified: 'Verified',

    // Role Comparison
    compareSectionTag: 'Contextual Analysis',
    compareTitle: 'Role-dependent evaluation',
    compareSubtitle: 'The same GitHub profile is evaluated completely differently depending on the role. There is no generic "coder score" — only role-specific readiness.',
    compareRole1: 'Backend Developer',
    compareRole1Score: '91%',
    compareRole1Tier: 'Ready',
    compareRole2: 'Frontend Developer',
    compareRole2Score: '64%',
    compareRole2Tier: 'Developing',
    compareRole3: 'DevOps / Cloud Engineer',
    compareRole3Score: '42%',
    compareRole3Tier: 'Not Ready',

    // Missing Skills & Gaps
    missingSectionTag: 'Growth Areas',
    missingTitle: 'Identify gaps constructively',
    missingSubtitle: 'Skills not yet found in your code are treated not as failures, but as actionable learning opportunities. You can also prove skills via quick interactive assessments.',
    missingCardFoundTitle: 'Evidenced in Code',
    missingCardFoundDesc: 'Technical capabilities identified and verified across your public projects.',
    missingCardNotYetTitle: 'Not Yet Evidenced',
    missingCardNotYetDesc: 'Areas expected for the target role that are not yet directly evidenced in your repositories.',
    missingInteractiveBadge: 'Interactive Proof',
    missingInteractiveDesc: 'Click "Prove this skill" to answer a targeted question and immediately verify your competency.',

    // Sample Analysis Section
    sampleSectionTag: 'Live Demo',
    sampleTitle: 'Explore a sample analysis',
    sampleSubtitle: 'Explore the deep insights SkillLens provides using our synthetic demo profile before analyzing your own.',
    sampleProfileUser: '@demo-developer',
    sampleProfileRole: 'Backend Developer · Mid-Level',
    sampleReadiness: '78% Ready',
    sampleRepos: '3 repositories reviewed',
    sampleActionBtn: 'View sample analysis',
    sampleSyntheticTag: 'Synthetic Demo',
    demoBannerLabel: 'Demo Analysis · Synthetic demo data, not real user data',

    // Personas Section
    personasSectionTag: 'Who It Is For',
    personasTitle: 'Clarity for every stage of your career',
    personasSubtitle: 'Whether you are a Junior preparing for your first role or a Mid-level engineer aiming for Senior.',
    persona1Title: 'Junior Developers',
    persona1Desc: 'Identify gaps before sending job applications and align your portfolio directly with industry expectations.',
    persona2Title: 'Mid-Level Engineers',
    persona2Desc: 'Discover which architectural patterns, testing standards, and system design signals you need for Senior roles.',
    persona3Title: 'Self-Taught & Career Switchers',
    persona3Desc: 'Validate your self-taught projects and practical engineering capabilities with objective, data-backed evidence.',

    // Trust & Security Section
    trustSectionTag: 'Privacy & Security',
    trustTitle: 'Transparent and secure evaluation principles',
    trustSubtitle: 'We are completely transparent about how your data and code are accessed.',
    trustPillar1Title: 'Read-Only Public Access',
    trustPillar1Desc: 'Only publicly accessible GitHub repositories are scanned. We never request access to your private repositories.',
    trustPillar2Title: 'Zero Write Permissions',
    trustPillar2Desc: 'No write, commit, or modification permissions are ever requested or needed for your account or code.',
    trustPillar3Title: 'Optional API Token',
    trustPillar3Desc: 'GitHub Personal Access Tokens are only used session-scoped to increase GitHub hourly API rate limits.',
    trustPillar4Title: 'Source Transparency',
    trustPillar4Desc: 'Assessments are grounded strictly in your chosen target role and detected code signals. CV/LinkedIn fusion is currently in development.',

    // Final CTA & Footer
    ctaTitle: 'How close are you to your target role?',
    ctaSubtitle: 'Enter your GitHub username to get a tailored skill readiness report in seconds.',
    ctaAnalyzeBtn: 'Analyze now',
    ctaSampleBtn: 'Explore sample analysis',
    footerTagline: 'Developer role readiness and codebase evidence assessment platform.',
    footerRights: 'All rights reserved.',
    footerPrivacyNote: 'SkillLens is an independent developer tool that analyzes public GitHub repositories against target role standards.',

    // Loading
    loadingTitle: 'Analyzing profile',
    loadingStep1: 'Connecting to GitHub',
    loadingStep2: 'Collecting repositories',
    loadingStep3: 'Reviewing projects',
    loadingStep4: 'Evaluating skills',
    loadingStep5: 'Preparing results',
    loadingRepositories: 'repositories',
    loadingFiles: 'files',

    // Dashboard
    dashboardTitle: 'Analysis',
    dashboardAnalyzedOn: 'Analysis from',
    dashboardRepoCount: 'repositories',
    dashboardFilesReviewed: 'files reviewed',
    dashboardRelevantRepos: 'relevant repos',
    dashboardReadiness: 'Readiness',
    dashboardReadinessDesc: {
      not_ready: 'The GitHub profile does not yet reflect the majority of skills expected for this role.',
      developing: 'Core skills are visible but several critical areas could not yet be verified.',
      approaching: 'The profile shows a good foundation for this role. A few important areas can be further developed.',
      ready: 'The majority of skills expected for this role appear to be verified in the GitHub profile.',
      exceeds: 'The profile demonstrates depth and breadth that exceeds the expected level for this role.',
    } as Record<string, string>,

    // Summary cards
    summaryRepositories: 'Repositories',
    summarySkills: 'Skills',
    summaryCoreSkills: 'Core skills',

    // Skills
    skillsOverviewTitle: 'Skills overview',
    skillsBreakdownTitle: 'Skills breakdown',
    skillsEvidenced: 'evidenced',

    // Evidence
    evidenceFound: 'Evidence found',
    evidenceClaimed: 'Claimed',
    evidenceClaimedDesc: 'Listed in CV or LinkedIn, but not verified in the analyzed repositories.',
    evidenceNotYet: 'Not yet evidenced',
    evidenceNotYetDesc: 'No supporting evidence was found in the analyzed sources.',
    evidenceSources: 'Supporting evidence',
    evidenceMore: 'more',
    evidenceProveSkill: 'Prove this skill',

    // Repos
    reposTitle: 'Repositories',
    repoStars: 'Stars',
    repoLanguages: 'Languages',
    repoRelevance: 'Relevance',
    repoRelevant: 'Relevant',
    repoNotRelevant: 'Not relevant',
    repoFiles: 'files',
    repoViewOnGitHub: 'View on GitHub',
    repoEvidenceFound: 'Evidence found',
    repoRelevantFor: 'Relevant for',

    // Tiers
    tierNotReady: 'Not Ready',
    tierDeveloping: 'Developing',
    tierApproaching: 'Approaching',
    tierReady: 'Ready',
    tierExceeds: 'Exceeds',

    // Errors
    errorGeneral: 'Analysis failed',
    errorRetry: 'Retry',
    errorGithubNotFound: 'GitHub user not found.',
    errorRateLimit: 'Rate limit exceeded. Please try again later.',
    errorTimeout: 'Request timed out.',

    // Empty states
    emptyNoEvidence: 'No evidence found',
    emptyNoEvidenceDesc: "This skill could not be verified from the repositories included in this analysis.",
    emptyNoRepos: 'No relevant repositories',
    emptyNoReposDesc: 'None of the analyzed repositories provided enough information for this role.',
    emptyAnalysisError: 'Analysis unavailable',

    // Assessment
    assessmentTitle: 'Assessment',
    assessmentQuestion: 'Question',
    assessmentOf: 'of',
    assessmentSubmit: 'Submit answer',
    assessmentContinue: 'Continue',
    assessmentYourAnswer: 'Your answer',
    assessmentCorrect: 'Correct',
    assessmentPartial: 'Partially correct',
    assessmentIncorrect: 'Incorrect',

    // Misc
    loading: 'Loading...',
    optional: 'Optional',
  },
} as const;

export type TranslationKey = keyof typeof translations.tr;

let currentLocale: Locale = 'tr';

export function getLocale(): Locale {
  return currentLocale;
}

export function setLocale(locale: Locale): void {
  currentLocale = locale;
  if (typeof window !== 'undefined') {
    localStorage.setItem('skilllens-locale', locale);
    window.dispatchEvent(new CustomEvent('locale-change', { detail: locale }));
  }
}

export function initLocale(): void {
  if (typeof window !== 'undefined') {
    const saved = localStorage.getItem('skilllens-locale') as Locale | null;
    if (saved === 'tr' || saved === 'en') {
      currentLocale = saved;
    }
  }
}

export function t(key: TranslationKey): string {
  const val = translations[currentLocale][key];
  if (typeof val === 'string') return val;
  return key;
}

export function tTierLabel(tier: string, locale?: Locale): string {
  const l = locale ?? currentLocale;
  const map: Record<string, { tr: string; en: string }> = {
    not_ready:  { tr: 'Hazır Değil', en: 'Not Ready' },
    developing: { tr: 'Gelişiyor',   en: 'Developing' },
    approaching:{ tr: 'Yaklaşıyor',  en: 'Approaching' },
    ready:      { tr: 'Hazır',       en: 'Ready' },
    exceeds:    { tr: 'Üstünde',     en: 'Exceeds' },
  };
  return map[tier]?.[l] ?? tier;
}

export function tReadinessDesc(tier: string, locale?: Locale): string {
  const l = locale ?? currentLocale;
  const desc = translations[l].dashboardReadinessDesc;
  return desc[tier] ?? '';
}

export function tLevelLabel(level: string, locale?: Locale): string {
  const l = locale ?? currentLocale;
  const map: Record<string, { tr: string; en: string }> = {
    junior: { tr: 'Junior', en: 'Junior' },
    mid:    { tr: 'Mid',    en: 'Mid' },
    senior: { tr: 'Senior', en: 'Senior' },
  };
  return map[level]?.[l] ?? level;
}

export function formatDate(isoString: string, locale?: Locale): string {
  const l = locale ?? currentLocale;
  try {
    const date = new Date(isoString);
    return date.toLocaleDateString(l === 'tr' ? 'tr-TR' : 'en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch {
    return isoString;
  }
}
