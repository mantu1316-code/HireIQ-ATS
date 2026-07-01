@echo off
echo ========================================
echo Starting HireIQ Backend Server
echo ========================================
cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting server...
uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause