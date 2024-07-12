#!/bin/sh

# Apply any pending database schema changes based on model changes
python manage.py makemigrations 

# Apply those changes to the database
python manage.py migrate 

# Start the Django development server on all available network interfaces, port 8000
python manage.py runserver 0.0.0.0:8000
