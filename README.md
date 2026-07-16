# hotel-lite-

## Quick Start (Windows)

1. Create virtual environment (if not already created):

```powershell
python -m venv .venv
```

2. Activate virtual environment:

- PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- CMD:

```bat
.venv\Scripts\activate.bat
```

- Git Bash:

```bash
source .venv/Scripts/activate
```

3. Install dependencies and run server:

```powershell
pip install django
python manage.py runserver
```

## Compatibility Note

If you type `v1\scripts\activate` in PowerShell, this project now supports it via a profile compatibility function that redirects to `.venv`.
