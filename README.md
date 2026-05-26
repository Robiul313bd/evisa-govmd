# Django eVisa Project

A fully functional Django project for entry visa to the Republic of Moldova.

## 📁 Project Structure

```
evisa-govmd/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database (auto-created)
│
├── core/                    # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── visa/                    # Main Django app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routing
│   ├── admin.py
│   └── tests.py
│
├── templates/               # HTML templates
│   ├── index.html           # Home page template
│   └── check-visa.html      # Check visa page template
│
└── static/                  # Static files
    ├── css/
    │   ├── main.css         # Index page styling
    │   └── style.css        # Check visa page styling
    ├── js/
    │   └── check-visa.js    # Visa check functionality
    └── assets/              # Images and other assets
        ├── logo.png
        ├── flag-md.png
        ├── flag-gb.png
        ├── header.png
        ├── headerb.jpg
        └── person.jpg
```

## 🚀 Setup Instructions

### Step 1: Create Virtual Environment

**On Windows (PowerShell or Command Prompt):**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 2: Install Django

Once the virtual environment is activated:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install Django==4.2.0
```

### Step 3: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 4: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 5: Create Superuser (Optional - for Django Admin)

```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 📄 File Descriptions

### **core/settings.py**
- `DEBUG = True` - Set to `False` for production
- `INSTALLED_APPS` - Added 'visa' app
- `TEMPLATES['DIRS']` - Configured to load from `templates/` folder
- `STATIC_URL` - Static files serve at `/static/`
- `STATICFILES_DIRS` - Points to `static/` directory
- `STATIC_ROOT` - Compiled static files location

### **visa/views.py**
- `index()` - Renders the home page (index.html)
- `check_visa()` - Renders the check visa page (check-visa.html)

### **visa/urls.py**
- `/` → index page
- `/check-visa/` → check visa page

### **Templates**

#### **templates/index.html**
- Converted from static HTML to Django template
- Uses `{% load static %}` to load CSS, JS, and images
- Uses `{% url %}` template tag for navigation links
- All image paths updated to use `{% static %}`

#### **templates/check-visa.html**
- Converted from static HTML to Django template
- Includes visa check form with captcha validation
- Dynamic result display functionality
- Modal alerts for user feedback

### **Static Files**

#### **CSS Files**
- `static/css/main.css` - Styling for index page
- `static/css/style.css` - Styling for check-visa page
- Both are responsive and mobile-friendly

#### **JavaScript**
- `static/js/check-visa.js` - Captcha generation and validation
  - `generateCaptcha()` - Generates random 6-character code
  - `showAlert()` - Displays error/success modals
  - `showVisaResult()` - Displays visa check results
  - Form validation and submission handling

#### **Assets**
- `logo.png` - Moldova coat of arms
- `flag-md.png` - Moldova flag
- `flag-gb.png` - UK flag
- `header.png` - Header banner
- `headerb.jpg` - Header background
- `person.jpg` - Sample visa holder photo

## 🌐 URLs

After running the server, access:

| URL | Page | Function |
|-----|------|----------|
| `http://localhost:8000/` | Index/Home | Main visa information page |
| `http://localhost:8000/check-visa/` | Check Visa | Visa status lookup form |
| `http://localhost:8000/admin/` | Admin Panel | Django administration (if superuser created) |

## 🎨 UI Features

✅ **Responsive Design** - Works on desktop, tablet, and mobile
✅ **Ministry Header** - Logo, title, and language flags
✅ **Navigation Bar** - Color-coded menu items
✅ **Sidebar** - Information boxes
✅ **Main Content** - Visa information and forms
✅ **Form Validation** - Real-time captcha and input checking
✅ **Modal Alerts** - User-friendly error/success messages
✅ **Dynamic Content** - Visa result display with applicant info
✅ **Footer** - Version and contact information

## 📋 Important Configuration

### **STATIC_URL vs STATICFILES_DIRS**

In `core/settings.py`:
```python
STATIC_URL = '/static/'  # URL prefix for serving static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Where Django looks for static files
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Where collectstatic compiles files
```

### **Template Tags**

In templates:
```html
{% load static %}
<!-- Load CSS -->
<link rel="stylesheet" href="{% static 'css/main.css' %}">

<!-- Load images -->
<img src="{% static 'assets/logo.png' %}" alt="Logo">

<!-- Load JavaScript -->
<script src="{% static 'js/check-visa.js' %}"></script>

<!-- Load URLs dynamically -->
<a href="{% url 'index' %}">Home</a>
<a href="{% url 'check_visa' %}">Check Visa</a>
```

## 🔧 Django Management Commands

```bash
# Show all available commands
python manage.py help

# Apply database migrations
python manage.py migrate

# Create new migration for model changes
python manage.py makemigrations

# Check project for issues
python manage.py check

# Create superuser account
python manage.py createsuperuser

# Collect static files for production
python manage.py collectstatic

# Run development server
python manage.py runserver [port]

# Access Django shell
python manage.py shell

# Generate random SECRET_KEY
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🛡️ Production Deployment Checklist

Before deploying to production:

1. **Change DEBUG to False** in `settings.py`
2. **Generate new SECRET_KEY** - Don't use the default
3. **Set ALLOWED_HOSTS** - Add your domain/IP
4. **Use PostgreSQL** instead of SQLite
5. **Use environment variables** for sensitive data
6. **Set up HTTPS** - Use SSL certificates
7. **Configure CORS** if needed
8. **Run security checks:**
   ```bash
   python manage.py check --deploy
   ```

## 🐛 Troubleshooting

### Static files not loading?
```bash
python manage.py collectstatic --clear --noinput
```

### Port already in use?
```bash
python manage.py runserver 8001
```

### Database errors?
```bash
python manage.py migrate --run-syncdb
```

### Permission issues?
```bash
# On Windows, clear __pycache__
Get-ChildItem -Path . -Include __pycache__ -Recurse -Force | Remove-Item -Recurse -Force
```

## 📞 Contact & Support

**Email:** evisa@mfa.gov.md  
**Ministry:** Ministry of Foreign Affairs and European Integration  
**Country:** Republic of Moldova

## 📝 License

This project is provided as-is for the Ministry of Foreign Affairs and European Integration of the Republic of Moldova.

---

**Django Version:** 4.2.0  
**Python Version:** 3.8+  
**Created:** 2026
