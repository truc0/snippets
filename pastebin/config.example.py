#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
SECRET_KEY = ''
ALLOWED_HOSTS = []

# DATABASE
# comment everything about database if you want
# to config database with environment vars

# using POSTGRESQL
"""
POSTGRES_HOST = ''
POSTGRES_NAME = ''
POSTGRES_PORT = 5432
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
"""

# or config manually
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
