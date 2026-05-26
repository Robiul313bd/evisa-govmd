# 📋 Django eVisa Project - Complete File Reference

## 🎯 Project Overview

Your static HTML website has been successfully converted to a fully functional Django project with:
- ✅ Virtual environment setup instructions
- ✅ Proper Django project structure
- ✅ One app (visa)
- ✅ Templates with `{% static %}` tags
- ✅ Static files organized (css, js, assets)
- ✅ URL routing configured
- ✅ Views.py with page rendering
- ✅ All HTML converted to Django templates
- ✅ UI design preserved exactly as original

---

## 📂 Complete Project Structure

```
evisa-govmd/
│
├── 📄 SETUP FILES
│   ├── manage.py                    ← Django management script (RUN ALL COMMANDS WITH THIS)
│   ├── requirements.txt             ← Python dependencies (Django 4.2.0)
│   ├── setup-windows.bat            ← Automated setup for Windows
│   ├── setup-linux-macos.sh         ← Automated setup for macOS/Linux
│   ├── README.md                    ← Full documentation (THIS FILE)
│   ├── QUICKSTART.md                ← Quick setup guide
│   └── PROJECT_STRUCTURE.md         ← This file (complete reference)
│
├── 📁 DJANGO CORE (Project Configuration)
│   └── core/
│       ├── __init__.py              ← Python package marker
│       ├── settings.py              ← Django configuration ⭐ IMPORTANT
│       ├── urls.py                  ← Main URL router (maps all URLs)
│       ├── asgi.py                  ← ASGI application (for async servers)
│       └── wsgi.py                  ← WSGI application (for production)
│
├── 📁 DJANGO APP (Your Visa App)
│   └── visa/
│       ├── __init__.py              ← Python package marker
│       ├── apps.py                  ← App configuration
│       ├── models.py                ← Database models (future extension)
│       ├── views.py                 ← View functions ⭐ PAGE RENDERERS
│       ├── urls.py                  ← App-specific URLs ⭐ ROUTES
│       ├── admin.py                 ← Django admin configuration
│       └── tests.py                 ← Unit tests
│
├── 📁 TEMPLATES (HTML Pages - Django Format)
│   └── templates/
│       ├── index.html               ← Home page (converted to Django)
│       └── check-visa.html          ← Visa check page (converted to Django)
│
├── 📁 STATIC FILES (CSS, JS, Images)
│   └── static/
│       ├── css/
│       │   ├── main.css             ← Index page styling
│       │   └── style.css            ← Check visa page styling
│       ├── js/
│       │   └── check-visa.js        ← Captcha & form validation
│       └── assets/
│           ├── logo.png             ← Ministry logo
│           ├── flag-md.png          ← Moldova flag
│           ├── flag-gb.png          ← UK flag
│           ├── header.png           ← Header image
│           ├── headerb.jpg          ← Header background
│           └── person.jpg           ← Sample visa photo
│
├── 📁 ORIGINAL FILES (Kept for Reference)
│   ├── index.html                   ← Original static HTML
│   ├── check-visa.html              ← Original static HTML
│   ├── assets/                      ← Original images
│   ├── css/                         ← Original stylesheets
│   └── js/                          ← Original JavaScript
│
└── 🗄️ DATABASE
    └── db.sqlite3                   ← Auto-created after first migration
```

---

## 📄 Key Files Explained

### 1️⃣ **manage.py** - Django Command Center
```bash
# Usage:
python manage.py [command]

# Common commands:
python manage.py runserver          # Start development server
python manage.py migrate            # Apply database migrations
python manage.py createsuperuser    # Create admin user
python manage.py collectstatic      # Gather static files for production
python manage.py shell              # Interactive Python shell
```

### 2️⃣ **core/settings.py** - Project Configuration
Contains all Django settings:
- `DEBUG = True` - Development mode (change to False for production)
- `INSTALLED_APPS` - Includes 'visa' app
- `TEMPLATES['DIRS']` - Points to `templates/` folder
- `STATIC_URL` - URL prefix for static files (`/static/`)
- `STATICFILES_DIRS` - Where Django finds static files
- `DATABASES` - SQLite configuration

### 3️⃣ **core/urls.py** - Main URL Router
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visa.urls')),  # All /visa app URLs
]
```

### 4️⃣ **visa/views.py** - Page Renderers
```python
def index(request):
    return render(request, 'index.html')    # Renders home page

def check_visa(request):
    return render(request, 'check-visa.html')  # Renders visa check page
```

### 5️⃣ **visa/urls.py** - App URL Routes
```python
urlpatterns = [
    path('', views.index, name='index'),              # / → index page
    path('check-visa/', views.check_visa, name='check_visa'),  # /check-visa/
]
```

### 6️⃣ **requirements.txt** - Dependencies
```
Django==4.2.0
```
Install with: `pip install -r requirements.txt`

---

## 🎨 Template Changes

### Original HTML vs Django Templates

#### **Before (Static HTML):**
```html
<link rel="stylesheet" href="css/main.css">
<img src="assets/logo.png">
<script src="js/check-visa.js"></script>
```

#### **After (Django Template):**
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/main.css' %}">
<img src="{% static 'assets/logo.png' %}">
<script src="{% static 'js/check-visa.js' %}"></script>
```

### Navigation Links Updated
```html
<!-- Before -->
<a href="./index.html">Start</a>

<!-- After (Dynamic URLs) -->
<a href="{% url 'index' %}">Start</a>
```

---

## 🚀 Setup & Execution Summary

### Windows Setup:
```batch
# Option 1: Automated (Recommended)
setup-windows.bat

# Option 2: Manual
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### macOS/Linux Setup:
```bash
# Option 1: Automated (Recommended)
chmod +x setup-linux-macos.sh
./setup-linux-macos.sh

# Option 2: Manual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Access the Application:
- **Home:** http://127.0.0.1:8000/
- **Check Visa:** http://127.0.0.1:8000/check-visa/
- **Admin:** http://127.0.0.1:8000/admin/ (if superuser created)

---

## 📊 URL Mapping Reference

| URL | View Function | Template | Purpose |
|-----|---------------|----------|---------|
| `/` | `index()` | `index.html` | Home page with visa information |
| `/check-visa/` | `check_visa()` | `check-visa.html` | Visa status lookup form |
| `/admin/` | Django Built-in | - | Django Administration |
| `/static/...` | Django Built-in | - | CSS, JS, Images (auto-served) |

---

## 📝 Static Files Reference

### CSS Files:
- **static/css/main.css** (2.5 KB)
  - Styling for index.html
  - Responsive design (mobile, tablet, desktop)
  - Header, navbar, sidebar, main content, footer

- **static/css/style.css** (3.8 KB)
  - Styling for check-visa.html
  - Form styling with captcha
  - Modal alerts and notifications
  - Result card display

### JavaScript Files:
- **static/js/check-visa.js** (2.3 KB)
  - Captcha generation: `generateCaptcha()`
  - Form validation: Checks visa number and verification code
  - Error alerts: `showAlert(title, message)`
  - Result display: `showVisaResult()`
  - Modal handling: `closeModal()`

### Image Assets:
- **logo.png** - Moldova coat of arms
- **flag-md.png** - Moldova flag (30×20px)
- **flag-gb.png** - UK flag (30×20px)
- **header.png** - "Visa Moldova" header graphic
- **headerb.jpg** - Header background image
- **person.jpg** - Sample applicant photo

---

## 🔄 Django Request Flow

```
User Request
    ↓
core/urls.py (Router)
    ↓
visa/urls.py (Routes to appropriate view)
    ↓
visa/views.py (index() or check_visa())
    ↓
templates/index.html or check-visa.html
    ↓
{% static %} tags load CSS/JS/Images
    ↓
HTML Response to Browser
```

---

## 🔐 Security Considerations

### Development (DEBUG=True):
- Django serves static files automatically
- Detailed error pages displayed
- Good for development

### Production (DEBUG=False):
- Run `python manage.py collectstatic`
- Use production web server (Gunicorn, uWSGI)
- Change `SECRET_KEY` in settings.py
- Set appropriate `ALLOWED_HOSTS`
- Use HTTPS/SSL
- Use PostgreSQL instead of SQLite

---

## ✅ Conversion Checklist

- ✅ Django project created (`core/`)
- ✅ Visa app created (`visa/`)
- ✅ Settings.py configured with:
  - ✅ 'visa' in INSTALLED_APPS
  - ✅ TEMPLATES['DIRS'] = ['templates']
  - ✅ STATIC_URL and STATICFILES_DIRS configured
- ✅ Templates folder created with Django templates
  - ✅ {% load static %} tags added
  - ✅ All paths converted to {% static %} format
  - ✅ Navigation updated to {% url %} format
- ✅ Static files organized:
  - ✅ static/css/ (main.css, style.css)
  - ✅ static/js/ (check-visa.js)
  - ✅ static/assets/ (all images copied)
- ✅ Views.py created with index and check_visa views
- ✅ URLs configured for routing
- ✅ UI design preserved exactly
- ✅ JavaScript functionality maintained
- ✅ Responsive design intact
- ✅ Setup scripts created (Windows & macOS/Linux)
- ✅ Documentation completed

---

## 🎓 What Changed vs What Stayed the Same

### Changed:
- ❌ HTML files moved to `templates/` folder
- ❌ Static files moved to `static/` folder
- ❌ Relative paths converted to `{% static %}` tags
- ❌ Navigation links use Django `{% url %}` tag
- ✅ Added Django-specific project files

### Stayed the Same:
- ✅ HTML structure identical
- ✅ CSS styling identical
- ✅ JavaScript functionality identical
- ✅ Visual design identical
- ✅ Form validation identical
- ✅ Responsive design identical
- ✅ All images identical

---

## 📞 Quick Reference Commands

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Run development server (default port 8000)
python manage.py runserver

# Run on specific port
python manage.py runserver 8001

# Check project health
python manage.py check

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Open Python shell
python manage.py shell

# Delete database (WARNING: Deletes all data)
rm db.sqlite3

# Deactivate virtual environment
deactivate
```

---

## 📚 Additional Resources

- **Django Official Docs:** https://docs.djangoproject.com/
- **Django Static Files:** https://docs.djangoproject.com/en/4.2/howto/static-files/
- **Django Templates:** https://docs.djangoproject.com/en/4.2/topics/templates/
- **Django URLs:** https://docs.djangoproject.com/en/4.2/topics/http/urls/

---

## 🎉 You're All Set!

Your Django eVisa project is ready to use. All files are in place, the structure is correct, and you have both automated and manual setup options.

**Next Step:** Run the setup script or follow the manual setup in QUICKSTART.md

---

**Date Created:** May 26, 2026
**Django Version:** 4.2.0
**Project Status:** ✅ Ready for Development
