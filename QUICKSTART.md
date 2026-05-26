# Quick Start Guide - Django eVisa Project

## For Windows Users:

### Option 1: Using Setup Script (Recommended)
```batch
setup-windows.bat
```

### Option 2: Manual Setup
```batch
# Step 1: Create virtual environment
python -m venv venv

# Step 2: Activate virtual environment
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run migrations
python manage.py migrate

# Step 5: Collect static files
python manage.py collectstatic --noinput

# Step 6: Run the server
python manage.py runserver
```

---

## For macOS/Linux Users:

### Option 1: Using Setup Script (Recommended)
```bash
chmod +x setup-linux-macos.sh
./setup-linux-macos.sh
```

### Option 2: Manual Setup
```bash
# Step 1: Create virtual environment
python3 -m venv venv

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run migrations
python manage.py migrate

# Step 5: Collect static files
python manage.py collectstatic --noinput

# Step 6: Run the server
python manage.py runserver
```

---

## Accessing the Application:

✅ **Home Page:** http://127.0.0.1:8000/
✅ **Check Visa:** http://127.0.0.1:8000/check-visa/
✅ **Admin Panel:** http://127.0.0.1:8000/admin/ (requires superuser)

---

## Create Superuser (Optional):

If you want to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Then login at: http://127.0.0.1:8000/admin/

---

## Common Issues:

### Port 8000 already in use?
```bash
python manage.py runserver 8001
```

### Static files not showing?
```bash
python manage.py collectstatic --clear --noinput
```

### Virtual environment activation fails?
Check that you're in the project directory:
```bash
cd path/to/evisa-govmd
```

---

## Project URLs:

- **Index Page:** Maps to `/` - Shows visa information
- **Check Visa Page:** Maps to `/check-visa/` - Visa status lookup
- **Admin:** Maps to `/admin/` - Django administration

---

For more details, see **README.md**
