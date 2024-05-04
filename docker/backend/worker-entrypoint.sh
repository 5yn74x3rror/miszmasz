#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A home worker --loglevel=info --concurrency 1 -E
