# petstagram

A Django learning project for a social app focused on pets and photo sharing.

## Project status

This repository currently contains the initial project scaffold:

- Django project configuration is in `petstagram/`
- App modules are prepared for `accounts`, `common`, `pets`, and `photos`
- Shared HTML templates are already added under `templates/`
- SQLite is configured as the default development database
- The admin route is available at `/admin/`

At this stage, the apps still contain starter files and can be extended incrementally.

## Tech stack

- Python 3
- Django 5.2.12
- SQLite3

## Project structure

```text
petstagram_now/
├── manage.py
├── requirements.txt
├── petstagram/
│   ├── settings.py
│   ├── urls.py
│   ├── accounts/
│   ├── common/
│   ├── pets/
│   └── photos/
└── templates/
    ├── accounts/
    ├── common/
    ├── pets/
    └── photos/
```

## Getting started

### 1. Clone the repository

```bash
git clone git@github.com:wako8o/petstagram.git
cd petstagram
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Then open:

- `http://127.0.0.1:8000/admin/`

## Optional: create an admin user

```bash
python manage.py createsuperuser
```

## Installed local apps

- `petstagram.accounts`
- `petstagram.common`
- `petstagram.pets`
- `petstagram.photos`

## Templates

The project includes shared templates in the root `templates/` directory, grouped by feature:

- `templates/accounts/`
- `templates/common/`
- `templates/pets/`
- `templates/photos/`

## Development notes

- `DEBUG = True` is enabled for local development.
- `db.sqlite3` is used locally and is ignored by Git.
- The secret key in `settings.py` should be moved to environment variables before production deployment.
- `ALLOWED_HOSTS` is currently empty and should be configured for deployment.

## Useful commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Next steps

Some natural next improvements for the project are:

- Add URL routing for the local apps
- Implement models for pets, photos, and profiles
- Connect the existing templates to real views
- Add tests for the main flows
