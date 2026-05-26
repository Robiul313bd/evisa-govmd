@echo off
REM Windows Setup Script for Django eVisa Project

echo.
echo ========================================
echo   Django eVisa Project Setup (Windows)
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [Step 1] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [Step 2] Activating virtual environment...
call venv\Scripts\activate.bat

echo [Step 3] Installing Django from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [Step 4] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Migration failed
    pause
    exit /b 1
)

echo [Step 5] Collecting static files...
python manage.py collectstatic --noinput
if errorlevel 1 (
    echo WARNING: Static file collection had issues
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Virtual Environment: venv
echo.
echo Next Steps:
echo 1. Create superuser (optional):
echo    python manage.py createsuperuser
echo.
echo 2. Run development server:
echo    python manage.py runserver
echo.
echo 3. Access the application:
echo    http://127.0.0.1:8000/
echo.
echo 4. Django Admin (if superuser created):
echo    http://127.0.0.1:8000/admin/
echo.
pause
