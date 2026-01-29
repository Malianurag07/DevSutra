@echo off
TITLE DevSutra Launcher

echo ========================================================
echo               DevSutra - Local Desktop Mode
echo ========================================================
echo.

:: 1. Check/Install Python Dependencies
echo [1/3] Checking Backend...
if not exist "venv" (
    echo    Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
echo    Installing requirements...
pip install -r requirements.txt > nul
echo    Applying migrations...
python manage.py migrate > nul

:: 2. Start Backend Server in a new window
echo.
echo [2/3] Starting Backend Server...
start "DevSutra Backend" cmd /k "call venv\Scripts\activate && python manage.py runserver"

:: 3. Start Frontend Server in a new window
echo.
echo [3/3] Starting Frontend Server...
cd frontend
if not exist "node_modules" (
    echo    Installing frontend dependencies (this may take a minute)...
    call npm install
)
start "DevSutra Frontend" cmd /k "npm run dev"

echo.
echo ========================================================
echo    SUCCESS! Application is running.
echo    Browser opening in 5 seconds...
echo ========================================================
echo.

timeout /t 5
start http://localhost:3000

exit
