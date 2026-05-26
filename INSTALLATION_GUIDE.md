# 🖥️ Detailed Installation Guide

## Prerequisites

- **Python 3.8 or higher** installed
- **Command line/Terminal** access
- **Text editor or IDE** (VS Code recommended)
- **Git** (optional, for version control)

---

## 🪟 Windows Installation (Detailed)

### Step 1: Verify Python Installation

Open **Command Prompt** or **PowerShell** and run:
```batch
python --version
```

**Expected Output:** `Python 3.x.x`

If you see "Python is not installed", download from: https://www.python.org/downloads/

### Step 2: Navigate to Project Directory

```batch
cd C:\Users\YourUsername\Downloads\evisa-govmd
```

Replace `YourUsername` with your actual Windows username.

### Step 3: Create Virtual Environment

```batch
python -m venv venv
```

This creates a folder named `venv` (virtual environment).

### Step 4: Activate Virtual Environment

```batch
venv\Scripts\activate
```

**You should see `(venv)` prefix in your terminal**, like:
```
(venv) C:\Users\YourUsername\Downloads\evisa-govmd>
```

### Step 5: Upgrade pip (Optional but Recommended)

```batch
python -m pip install --upgrade pip
```

### Step 6: Install Django

```batch
pip install -r requirements.txt
```

Or install directly:
```batch
pip install Django==4.2.0
```

Verify installation:
```batch
django-admin --version
```

### Step 7: Apply Database Migrations

```batch
python manage.py migrate
```

You should see output like:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
```

### Step 8: Collect Static Files

```batch
python manage.py collectstatic --noinput
```

### Step 9: Create Superuser (Optional)

```batch
python manage.py createsuperuser
```

You'll be asked for:
- Username: `admin`
- Email: `admin@example.com`
- Password: `(type a password)`
- Confirm Password: `(retype password)`

### Step 10: Run Development Server

```batch
python manage.py runserver
```

**Expected Output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Step 11: Open Browser

Visit: **http://127.0.0.1:8000/**

You should see the Moldova eVisa home page!

### To Stop Server:
Press `Ctrl + C` in the terminal

### To Deactivate Virtual Environment:
```batch
deactivate
```

### To Reactivate Later:
```batch
venv\Scripts\activate
python manage.py runserver
```

---

## 🍎 macOS Installation (Detailed)

### Step 1: Verify Python Installation

Open **Terminal** and run:
```bash
python3 --version
```

**Expected Output:** `Python 3.x.x`

If not installed, install via Homebrew:
```bash
brew install python@3.11
```

### Step 2: Navigate to Project Directory

```bash
cd ~/Downloads/evisa-govmd
```

Or wherever you saved the project.

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

```bash
source venv/bin/activate
```

**You should see `(venv)` prefix**, like:
```
(venv) user@MacBook:~/Downloads/evisa-govmd %
```

### Step 5: Upgrade pip (Optional but Recommended)

```bash
python -m pip install --upgrade pip
```

### Step 6: Install Django

```bash
pip install -r requirements.txt
```

Or directly:
```bash
pip install Django==4.2.0
```

Verify:
```bash
django-admin --version
```

### Step 7-10: Same as Windows

Follow Steps 7-10 from Windows section above.

### Step 11: Open Browser

Visit: **http://127.0.0.1:8000/**

---

## 🐧 Linux Installation (Ubuntu/Debian)

### Step 1: Verify Python Installation

```bash
python3 --version
```

If not installed:
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

### Step 2: Navigate to Project Directory

```bash
cd ~/Downloads/evisa-govmd
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

```bash
source venv/bin/activate
```

### Step 5-10: Same as macOS/Windows

---

## ⚙️ Troubleshooting

### Problem: "Python is not recognized"

**Solution:** Python is not in your system PATH.
- **Windows:** Reinstall Python and check "Add Python to PATH"
- **Mac/Linux:** Use `python3` instead of `python`

### Problem: "No module named 'django'"

**Solution:** Virtual environment not activated or Django not installed.
```bash
# Make sure (venv) prefix is visible
# Then reinstall:
pip install Django==4.2.0
```

### Problem: Port 8000 already in use

**Solution:** Use different port:
```bash
python manage.py runserver 8001
```

Then visit: http://127.0.0.1:8001/

### Problem: Static files not loading (no CSS styling)

**Solution:** Collect static files:
```bash
python manage.py collectstatic --clear --noinput
```

### Problem: Permission denied on Linux/Mac setup script

**Solution:** Make script executable:
```bash
chmod +x setup-linux-macos.sh
./setup-linux-macos.sh
```

### Problem: "ModuleNotFoundError" or "ImportError"

**Solution:** 
1. Make sure virtual environment is activated (see `(venv)` prefix)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Clear Python cache: `find . -type d -name __pycache__ -exec rm -r {} +`

### Problem: Database errors

**Solution:** Reset database:
```bash
# Delete database file
rm db.sqlite3

# Re-create
python manage.py migrate
```

---

## 🎯 Common Commands Reference

| Task | Command |
|------|---------|
| Create venv (Windows) | `python -m venv venv` |
| Create venv (Mac/Linux) | `python3 -m venv venv` |
| Activate (Windows) | `venv\Scripts\activate` |
| Activate (Mac/Linux) | `source venv/bin/activate` |
| Deactivate | `deactivate` |
| Install requirements | `pip install -r requirements.txt` |
| Migrate database | `python manage.py migrate` |
| Collect static | `python manage.py collectstatic --noinput` |
| Run server | `python manage.py runserver` |
| Create admin user | `python manage.py createsuperuser` |
| Check project | `python manage.py check` |
| Clear cache | `find . -type d -name __pycache__ -delete` |

---

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Virtual environment created (`venv/` folder exists)
- [ ] Virtual environment activated (`(venv)` prefix visible)
- [ ] Django installed (`django-admin --version` works)
- [ ] Migrations applied (no database errors)
- [ ] Static files collected (`staticfiles/` folder created)
- [ ] Server running (no errors when starting)
- [ ] Home page loads (http://127.0.0.1:8000/)
- [ ] CSS/styling visible (not plain HTML)
- [ ] Images loading (logos and header visible)
- [ ] Check Visa page loads (http://127.0.0.1:8000/check-visa/)
- [ ] Forms functional (can enter text)
- [ ] Admin accessible (http://127.0.0.1:8000/admin/)

---

## 📱 Testing Different Screens

After running the server, test on different devices:

1. **Desktop:** http://127.0.0.1:8000/ (full width)
2. **Tablet:** Use browser DevTools (F12) → Tablet view
3. **Mobile:** Use browser DevTools (F12) → Mobile view

The site should be responsive and work properly on all screen sizes.

---

## 🚀 Next Steps After Installation

1. **Explore the Admin Panel:**
   - Visit http://127.0.0.1:8000/admin/
   - Login with superuser credentials
   - This is where you can manage users and content

2. **Review Project Files:**
   - Open `core/settings.py` to understand Django configuration
   - Open `visa/views.py` to see how pages are rendered
   - Open `templates/index.html` to see how templates work

3. **Modify Templates:**
   - Edit `templates/index.html` or `templates/check-visa.html`
   - Save and refresh browser (no server restart needed!)

4. **Modify CSS:**
   - Edit `static/css/main.css` or `static/css/style.css`
   - Refresh browser to see changes

5. **Extend the Project:**
   - Add more views in `visa/views.py`
   - Create new templates in `templates/`
   - Add more URLs in `visa/urls.py`

---

## 📖 Further Learning

- **Django Official Tutorial:** https://docs.djangoproject.com/en/4.2/intro/
- **Django Models:** https://docs.djangoproject.com/en/4.2/topics/db/models/
- **Django Forms:** https://docs.djangoproject.com/en/4.2/topics/forms/
- **Django Class-Based Views:** https://docs.djangoproject.com/en/4.2/topics/class-based-views/

---

## 🎓 Project Structure Learning Path

1. **Start with:** `manage.py` - Understand Django commands
2. **Then read:** `core/settings.py` - Learn project configuration
3. **Then read:** `visa/views.py` - Learn how views work
4. **Then read:** `templates/index.html` - Learn Django templates
5. **Then read:** `static/css/main.css` - Understand styling

---

**You're all set! Enjoy your Django eVisa project!** 🎉
