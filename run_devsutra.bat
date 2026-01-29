@echo off
TITLE DevSutra Launcher
CLS

echo.
echo  ========================================================
echo               DevSutra - Laptop App Mode
echo  ========================================================
echo.

:: 0. Prerequisite Check
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.10+ from python.org
    pause
    exit
)

node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed or not in PATH.
    echo Please install Node.js 18+ from nodejs.org
    pause
    exit
)

:: 1. Check/Install Python Dependencies
echo [1/3] Checking Backend System...
if not exist "venv" (
    echo    - Creating virtual environment (First run only)...
    python -m venv venv
)

:: Active venv and check packages
call venv\Scripts\activate
if not exist "venv\Lib\site-packages\django" (
    echo    - Installing required libraries...
    pip install -r requirements.txt > nul
    echo    - Setting up database...
    python manage.py migrate > nul
    python generate_problems.py > nul
    python manage.py import_problems > nul
)

:: 2. Start Backend Server (Minimized)
echo.
echo [2/3] Starting Backend Engine...
start "DevSutra Backend" /min cmd /k "call venv\Scripts\activate && python manage.py runserver"

:: 3. Start Frontend Server (Minimized)
echo.
echo [3/3] Starting Frontend Interface...
cd frontend
if not exist "node_modules" (
    echo    - Installing frontend modules (First run only, please wait)...
    call npm install > nul
)
start "DevSutra Frontend" /min cmd /k "npm run dev"

echo.
echo ========================================================
echo    APP IS RUNNING! 🚀
echo.
echo    Keep this window open. 
echo    Your browser will open automatically in 5 seconds.
echo ========================================================
echo.

timeout /t 5 > nul
start http://localhost:3000

:: Optional: Wait loop to keep main window alive
pause
exit
