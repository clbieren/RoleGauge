"""
Groq API Key Verification & Diagnostics Script.
Usage:
    .venv\\Scripts\\python.exe scripts\\test_groq_key.py
"""

import os
import sys
import time
import asyncio
import io

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

# Load backend directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.join(BASE_DIR, "backend")
sys.path.insert(0, backend_dir)

# Read .env file directly to check
env_path = os.path.join(backend_dir, ".env")
groq_key = None
groq_model = "llama-3.3-70b-versatile"

if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("GROQ_API_KEY=") and not line.startswith("#"):
                groq_key = line.split("=", 1)[1].strip()
            elif line.startswith("GROQ_MODEL=") and not line.startswith("#"):
                groq_model = line.split("=", 1)[1].strip()

# Also check os.environ override
groq_key = os.environ.get("GROQ_API_KEY", groq_key)
groq_model = os.environ.get("GROQ_MODEL", groq_model)

async def test_groq():
    print("==================================================")
    print("        RoleGauge — Groq API Test Aracı         ")
    print("==================================================")
    print(f"Model: {groq_model}")
    print(f"Env Dosyası: {env_path}\n")

    if not groq_key or groq_key == "BURAYA_GROQ_API_KEYINIZI_YAPISTIRIN":
        print("[!] GROQ_API_KEY henüz ayarlanmamış.")
        print(f"Lütfen '{env_path}' dosyasındaki:")
        print("    GROQ_API_KEY=BURAYA_GROQ_API_KEYINIZI_YAPISTIRIN")
        print("satırına Groq konsolundan aldığınız anahtarı (gsk_...) yapıştırın.")
        print("Ardından bu betiği tekrar çalıştırın:")
        print("    .venv\\Scripts\\python.exe scripts\\test_groq_key.py")
        return False

    masked_key = groq_key[:6] + "..." + groq_key[-4:] if len(groq_key) > 10 else "***"
    print(f"Tespit Edilen Anahtar: {masked_key}")
    print("Groq LPU API'sine bağlantı testi yapılıyor...")

    try:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(
            api_key=groq_key,
            base_url="https://api.groq.com/openai/v1",
            timeout=15,
        )

        start_time = time.perf_counter()
        resp = await client.chat.completions.create(
            model=groq_model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise JSON evaluator. Respond strictly with JSON."
                },
                {
                    "role": "user",
                    "content": "Verify connection and respond with {\"status\": \"ok\", \"ping\": \"pong\"}"
                }
            ],
            temperature=0.1,
            max_tokens=50,
        )
        duration_ms = (time.perf_counter() - start_time) * 1000

        content = resp.choices[0].message.content
        print(f"\n✓ BAĞLANTI BAŞARILI!")
        print(f"Yanıt Süresi: {duration_ms:.1f} ms")
        print(f"Kullanılan Model: {resp.model}")
        print(f"Kullanılan Token: prompt={resp.usage.prompt_tokens}, completion={resp.usage.completion_tokens}, total={resp.usage.total_tokens}")
        print(f"Model Yanıtı: {content.strip()}")
        print("\nRoleGauge backend AI analizi için Groq başarıyla devrede!")
        return True

    except Exception as e:
        print(f"\n[HATA] Groq API çağrısı başarısız oldu:")
        print(f"{type(e).__name__}: {e}")
        print("\nLütfen anahtarın doğruluğunu ve internet bağlantınızı kontrol edin.")
        return False

if __name__ == "__main__":
    asyncio.run(test_groq())
