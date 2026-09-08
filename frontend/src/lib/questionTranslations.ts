/**
 * SkillLens — Değerlendirme Soruları Türkçe Çevirileri
 * Soru metinlerini Türkçe olarak sunar, teknik terimlerin korunmasını sağlar.
 */

const QUESTION_MAP: Record<string, string> = {
  // Game Dev
  "What is the difference between additive and single scene loading?":
    "Additive (eklemeli) ile Single (tekli) sahne yükleme (scene loading) arasındaki temel fark nedir?",

  "Create a scene transition system that loads a new level with a fade-to-black effect while preserving the player's score.":
    "Oyuncunun skorunu koruyarak ve ekranda kararma (fade-to-black) geçişi uygulayarak yeni bir bölüm yükleyen bir sahne geçiş sistemi tasarlayın.",

  "What is the difference between a kinematic and a dynamic (rigid) body?":
    "Kinematik (kinematic) gövde ile dinamik (dynamic / rigidbody) gövde arasındaki fark nedir?",

  "Your character's attack animation doesn't transition smoothly back to idle. How would you debug this?":
    "Karakterinizin saldırı animasyonu bekleme (idle) durumuna akıcı bir şekilde geri dönmüyor. Bu sorunu nasıl ayıklar ve çözersiniz?",

  "Your game's draw call count is over 2000 and causing frame drops. What optimization strategies would you use?":
    "Oyununuzdaki draw call sayısı 2000'in üzerine çıktı ve FPS düşüşlerine neden oluyor. Hangi optimizasyon yöntemlerini (batching, instancing, culling vb.) kullanırsınız?",

  "Create a custom editor window that allows level designers to place waypoints on a navmesh and visualize the resulting AI patrol routes.":
    "Bölüm tasarımcılarının navmesh üzerine rota noktaları (waypoints) yerleştirmesini ve yapay zeka devriye rotalarını görselleştirmesini sağlayan özel bir editör aracı tasarlayın.",

  "You need to ship the same game on PC, Nintendo Switch, and mobile. What architectural decisions would you make to handle platform differences?":
    "Aynı oyunu PC, Nintendo Switch ve mobilde yayınlamanız gerekiyor. Platform farklılıklarını yönetmek için hangi mimari kararları alırsınız?",

  "Explain the game loop and the difference between Update and FixedUpdate (or _process and _physics_process).":
    "Oyun döngüsünü (game loop) açıklayın; Update ile FixedUpdate (veya _process ile _physics_process) arasındaki farkı ve ne zaman hangisinin kullanıldığını belirtin.",

  "You have 50 different enemy types that share some behaviors but differ in others. How would you structure this using OOP?":
    "Bazı davranışları ortak, bazıları ise farklılaşan 50 farklı düşman türünüz var. Bunu Nesne Yönelimli Programlama (OOP / bileşen mimarisi) kullanarak nasıl yapılandırırsınız?",

  "Your game's GC spikes are causing visible hitches every few seconds. How would you diagnose and fix this?":
    "Oyununuzda birkaç saniyede bir oluşan Garbage Collection (GC) bellek temizleme sıçramaları takılmalara yol açıyor. Bunu nasıl tespit eder ve optimize edersiniz?",

  "What are the advantages of ECS over traditional OOP for game development? What are the trade-offs?":
    "Oyun geliştirmede ECS (Entity Component System) mimarisinin geleneksel OOP'ye göre avantajları ve getirdiği ödünleşimler (trade-offs) nelerdir?",

  "Implement a simple arena allocator in C++ that can allocate memory blocks from a pre-allocated buffer and reset the entire arena at once.":
    "Önceden ayrılmış bir bellek bloğundan tahsis yapan ve tüm alanı tek seferde sıfırlayabilen bir arena allocator mantığını açıklayın.",

  "How would you use the dot product to determine if an enemy is in front of or behind the player?":
    "Bir düşmanın oyuncunun önünde mi yoksa arkasında mı olduğunu belirlemek için dot product (nokta çarpım) nasıl kullanılır?",

  "Why are Quaternions preferred over Euler angles for 3D rotations in game engines? What problem do they solve?":
    "Oyun motorlarında 3D döndürmeler için Quaternion'lar neden Euler açılarından daha çok tercih edilir? Hangi problemi (örn: Gimbal Lock) çözerler?",

  "Explain the Model-View-Projection (MVP) matrix pipeline and what each matrix does.":
    "Model-View-Projection (MVP) matris dönüşüm hattını ve her bir matrisin rolünü açıklayın.",

  "What is the difference between Lerp and Slerp? When would you use each?":
    "Lerp (Linear Interpolation) ile Slerp (Spherical Linear Interpolation) arasındaki fark nedir? Hangi durumlarda hangisi kullanılır?",

  "How do you calculate the angle between two 2D vectors? Write the mathematical formula or code.":
    "İki 2D vektör arasındaki açıyı nasıl hesaplarsınız? Matematiksel formülü veya kod yaklaşımını açıklayın.",

  "Your game has 10,000 entities checking collisions against each other. How would spatial partitioning reduce this from O(N^2)?":
    "Oyununuzda birbiriyle çarpışma testi yapan 10.000 nesne var. Uzamsal bölümleme (spatial partitioning / BVH / Quadtree) karmaşıklığı O(N^2)'den nasıl düşürür?",

  "Design the core loop for a tower defense game. What are the key mechanics and how do they create engagement?":
    "Bir kule savunma (tower defense) oyunu için temel oyun döngüsünü (core loop) tasarlayın. Temel mekanikler ve oyuncu bağlayıcılığı nasıl kurulur?",

  "Implement an FSM for an enemy with Idle, Patrol, Chase, and Attack states. Define the transitions between them.":
    "Idle, Patrol, Chase ve Attack durumlarına sahip bir düşman için Sonlu Durum Makinesi (FSM) tasarlayın ve durum geçişlerini tanımlayın.",

  "Describe the stages of the GPU rendering pipeline from vertex input to pixel output.":
    "Köşe noktalarından (vertex input) piksel çıktısına kadar GPU render hattının (rendering pipeline) temel aşamalarını açıklayın.",

  "What is the difference between a listen server and a dedicated server in multiplayer games?":
    "Çok oyunculu oyunlarda listen server (dinleyici sunucu) ile dedicated server (tahsisli sunucu) arasındaki fark nedir?",

  // Backend
  "Explain the difference between PUT and PATCH HTTP methods regarding resource replacement vs partial update idempotency. Why should a successful DELETE request return HTTP 204 No Content or HTTP 200 OK?":
    "HTTP PUT ve PATCH metotları arasındaki farkı (kaynak değişimi vs kısmi güncelleme / idempotency) açıklayın. Başarılı bir DELETE isteği neden 204 No Content veya 200 OK dönmelidir?",

  "Design a standardized REST API error response following RFC 7807 (Problem Details for HTTP APIs). What standard fields ('type', 'title', 'status', 'detail', 'instance', 'invalid_params') must be included when returning a 422 Unprocessable Entity for invalid input payloads?":
    "RFC 7807 (Problem Details) standardına uygun bir REST API hata yapısı tasarlayın. Geçersiz girdi (422 Unprocessable Entity) durumunda hangi standart alanlar yer almalıdır?",

  "Why does offset-based pagination ('OFFSET 100000 LIMIT 20') degrade in performance on large tables, and how does cursor-based / keyset pagination ('WHERE id > last_seen_id ORDER BY id ASC LIMIT 20') achieve constant-time O(1) pagination without missing newly inserted rows?":
    "Büyük tablolarda offset tabanlı sayfalama (OFFSET 100000) neden yavaşlar? Cursor-based (keyset) sayfalama O(1) erişim sağlayarak bu sorunu nasıl çözer?",

  "In a GraphQL API, querying a list of 100 users and their recent orders triggers 101 database queries. Explain how DataLoader batches and caches individual resolver requests within a single tick of the event loop to solve this GraphQL N+1 problem.":
    "GraphQL API'de 100 kullanıcı ve siparişlerini çekerken oluşan N+1 sorgu problemini DataLoader nasıl toplu (batch) ve önbellekli hale getirerek çözer?",

  "Compare embedding documents versus referencing (normalized IDs) in MongoDB for a blog post with comments. In what situation does document embedding hit the 16MB BSON limit or suffer from unbounded document growth?":
    "MongoDB'de yorumlu bir blog yazısı için belge gömme (embedding) ile referanslama (referencing) yöntemlerini karşılaştırın. Gömülü yapı hangi durumlarda 16MB sınırına takılır?",

  // Frontend
  "Explain the difference between React state and props. When should state be lifted up?":
    "React'ta State ile Props arasındaki farkı açıklayın. Durum (state) ne zaman bir üst bileşene taşınmalıdır (lifting state up)?",

  "What is the Virtual DOM and how does React's reconciliation algorithm optimize DOM updates?":
    "Virtual DOM nedir ve React'ın reconciliation (uzlaştırma) algoritması DOM güncellemelerini nasıl optimize eder?",

  "Explain the difference between useEffect, useMemo, and useCallback hooks. Give a concrete use case for each.":
    "useEffect, useMemo ve useCallback kancaları (hooks) arasındaki farkları açıklayın ve her biri için somut bir kullanım örneği verin.",

  "How does CSS Flexbox differ from CSS Grid? In what scenarios would you choose Grid over Flexbox?":
    "CSS Flexbox ile CSS Grid arasındaki farklar nelerdir? Hangi durumlarda Flexbox yerine Grid tercih edilmelidir?",

  "What are the Core Web Vitals (LCP, FID/INP, CLS) and how would you optimize an image-heavy page to achieve good scores?":
    "Core Web Vitals metrikleri (LCP, INP, CLS) nelerdir? Görsel ağırlıklı bir web sayfasını bu metriklerde yüksek puan alacak şekilde nasıl optimize edersiniz?",

  "Explain the difference between Server-Side Rendering (SSR), Static Site Generation (SSG), and Client-Side Rendering (CSR).":
    "Sunucu Taraflı Render (SSR), Statik Site Üretimi (SSG) ve İstemci Taraflı Render (CSR) arasındaki farkları ve kullanım senaryolarını açıklayın.",
};

/**
 * Verilen soru metnini aktif dile göre döndürür.
 * Türkçe seçiliyse ve çeviri varsa Türkçesini, yoksa orijinalini döner.
 */
export function getTranslatedQuestion(question: string, locale: string): string {
  if (locale !== 'tr') return question;
  return QUESTION_MAP[question] || QUESTION_MAP[question.trim()] || question;
}

/**
 * Sorunun Türkçe çevirisinin olup olmadığını kontrol eder.
 */
export function hasTurkishTranslation(question: string): boolean {
  return Boolean(QUESTION_MAP[question] || QUESTION_MAP[question.trim()]);
}
