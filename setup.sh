#!/bin/bash
python3 djangProj/manage.py makemigrations details
python3 djangProj/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 manage.py shell

