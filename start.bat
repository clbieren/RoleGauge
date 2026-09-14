@echo off
title RoleGauge Dev Server
echo ===================================================
echo           RoleGauge — Full Stack Baslatici
echo ===================================================
echo.
echo [1/2] Backend (FastAPI :8000) baslatiliyor...
start "RoleGauge Backend (Port 8000)" powershell -NoExit -Command ".venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --port 8000 --reload"

echo [2/2] Frontend (Next.js :3000) baslatiliyor...
start "RoleGauge Frontend (Port 3000)" powershell -NoExit -Command "npm --prefix frontend run dev"

echo.
echo ===================================================
echo  Backend:  http://127.0.0.1:8000 (API & Docs: /docs)
echo  Frontend: http://localhost:3000
echo ===================================================
echo Servisler calisiyor. Tarayicinizdan http://localhost:3000 adresine gidebilirsiniz.
