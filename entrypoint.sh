#!/bin/sh
if [ ! -f /app/data/lernkarten.db ]; then
  echo "Initializing Data Base"
  python init_database.py
  python migrate_from_json.py
fi

exec "$@"