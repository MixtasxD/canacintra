# Canacintra (Django)

Proyecto Django con app `core`, listo para desarrollo local y despliegue en Render usando base de datos Neon (PostgreSQL).

## Requisitos

- Python 3.12+ (Render usa 3.12.6; local puedes usar 3.11/3.12)
- pip
- Opcional local: MySQL si deseas usar la config antigua (ya no necesario para deploy)

## Instalación local (SQLite por defecto)

```bash
python3 -m venv canacintra_env
source canacintra_env/bin/activate
pip install -r requirements.txt
cd canacintra
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000/

## Usar Neon (PostgreSQL) en local (opcional)

1. Crea una DB en Neon y copia tu `DATABASE_URL` (formato: `postgresql://user:pass@host/db?sslmode=require`).
2. Exporta la variable y migra:

```bash
export DATABASE_URL="postgresql://<user>:<pass>@<host>/<db>?sslmode=require"
python manage.py migrate
python manage.py runserver
```

## Despliegue en Render

Este repo incluye `render.yaml`, `runtime.txt` y configuración en `settings.py` para:
- Static files con WhiteNoise
- `DATABASE_URL` (dj-database-url)
- Gunicorn como servidor WSGI

Pasos:
1. Sube el repo a GitHub.
2. En Render > New > Web Service > Conecta tu repo.
3. Define variables de entorno:
   - `DJANGO_SETTINGS_MODULE=canacintra.settings`
   - `DJANGO_SECRET_KEY` (cadena aleatoria)
   - `DATABASE_URL` (Neon, con `sslmode=require`)
4. Render ejecutará migraciones y `collectstatic` automáticamente.

## Variables de entorno

Copia `.env.example` a `.env` (para documentarlas) y define en Render como variables del servicio.

- `DJANGO_SECRET_KEY`: Secreto de Django
- `DATABASE_URL`: URL de conexión Postgres (Neon) con `sslmode=require`

## Estructura relevante

- `canacintra/` proyecto Django
- `canacintra/core/` app principal (templates, static)
- `blogy/` plantilla estática (no requerida para deploy)

## Licencia

Sin licencia definida. Añade una si lo deseas.