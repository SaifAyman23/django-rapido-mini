#!/bin/bash
set -e

# ===========================
# ENTRYPOINT FOR DJANGO + CELERY STACK
# Production-ready with organized sections for easy customization
# ===========================

echo "========================================="
echo "Container started: $(date)"
echo "========================================="

# ===========================
# 1. DETERMINE CONTAINER ROLE
# ===========================
# Set CONTAINER_ROLE in docker-compose.yml environment for each service
CONTAINER_ROLE=${CONTAINER_ROLE:-web}
echo "Container role: $CONTAINER_ROLE"

# ===========================
# 2. WAIT FOR DEPENDENCIES
# ===========================
echo ""
echo "Waiting for dependencies..."

# Wait for PostgreSQL
echo "  Checking PostgreSQL at ${DB_HOST:-db}:${DB_PORT:-5432}..."
max_retries=30
retry_count=0
while [ $retry_count -lt $max_retries ]; do
    if nc -z ${DB_HOST:-db} ${DB_PORT:-5432} 2>/dev/null; then
        echo "  ✓ PostgreSQL is ready"
        break
    fi
    retry_count=$((retry_count + 1))
    if [ $retry_count -lt $max_retries ]; then
        echo "    Attempt $retry_count/$max_retries..."
        sleep 2
    fi
done

if [ $retry_count -eq $max_retries ]; then
    echo "  ✗ PostgreSQL failed to start after $max_retries attempts"
    exit 1
fi

# ===========================
# 3. DJANGO SETUP (web and workers only)
# ===========================
if [ "$CONTAINER_ROLE" = "web" ] || [ "$CONTAINER_ROLE" = "celery_worker" ]; then
    echo ""
    echo "Running Django setup tasks..."
    
    # Collect static files
    echo "  Collecting static files..."
    python manage.py collectstatic --noinput --clear 2>&1 | grep -v "^Copying\|^Installed"
    
    # Create migrations
    echo "  Creating migrations..."
    python manage.py makemigrations --noinput 2>&1 | grep -v "No changes detected"
    
    # Apply migrations
    echo "  Applying migrations..."
    python manage.py migrate --noinput
    
    # Create superuser (local development only)
    if [ "${DJANGO_ENVIRONMENT:-local}" = "local" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
        echo "  Creating superuser..."
        python manage.py createsuperuser --noinput --username=${DJANGO_SUPERUSER_USERNAME:-admin} --email=${DJANGO_SUPERUSER_EMAIL:-admin@example.com} 2>/dev/null || echo "    (superuser may already exist)"
    fi
    
    echo "✓ Django setup complete"
fi

# ===========================
# 4. START THE APPROPRIATE SERVICE
# ===========================
echo ""
echo "Starting $CONTAINER_ROLE service..."
echo "========================================="
echo ""

case "$CONTAINER_ROLE" in
    web)
        if [ "${DJANGO_ENVIRONMENT:-local}" = "production" ]; then
            echo "Running Gunicorn (production mode)..."
            exec gunicorn project.wsgi:application \
                --bind 0.0.0.0:8000 \
                --workers 4 \
                --worker-class sync \
                --max-requests 1000 \
                --timeout 120 \
                --access-logfile - \
                --error-logfile -
        else
            echo "Running Django runserver (development mode)..."
            exec python manage.py runserver 0.0.0.0:8000
        fi
        ;;
    
    *)
        echo "ERROR: Unknown container role: $CONTAINER_ROLE"
        echo "Valid roles: web"
        exit 1
        ;;
esac