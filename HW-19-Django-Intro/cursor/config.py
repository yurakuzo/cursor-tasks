from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = bool(environ.get("DEBUG"))
ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS").split()

DB_NAME = environ.get("DB_NAME")
DB_USERNAME = environ.get("DB_USERNAME")
DB_PASSWORD = environ.get("DB_PASSWORD")
DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("DB_PORT")
