#!/bin/bash

# Linux/macOS Setup Script for Django eVisa Project

echo ""
echo "========================================"
echo "  Django eVisa Project Setup (macOS/Linux)"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[Step 1] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "[Step 2] Activating virtual environment..."
source venv/bin/activate

echo "[Step 3] Installing Django from requirements.txt..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[Step 4] Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Migration failed"
    exit 1
fi

echo "[Step 5] Collecting static files..."
python manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "WARNING: Static file collection had issues"
fi

echo ""
echo "========================================"
echo "   Setup Complete!"
echo "========================================"
echo ""
echo "Virtual Environment: venv"
echo ""
echo "Next Steps:"
echo "1. Create superuser (optional):"
echo "   python manage.py createsuperuser"
echo ""
echo "2. Run development server:"
echo "   python manage.py runserver"
echo ""
echo "3. Access the application:"
echo "   http://127.0.0.1:8000/"
echo ""
echo "4. Django Admin (if superuser created):"
echo "   http://127.0.0.1:8000/admin/"
echo ""
