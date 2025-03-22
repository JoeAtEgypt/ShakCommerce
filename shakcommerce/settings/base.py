import os
import mimetypes
from pathlib import Path

from shakcommerce.settings import security

# Identify the image extension
mimetypes.add_type("image/webp", ".webp")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Read the secret key from the file
SECRET_KEY = os.environ.get("SECRET_KEY")

# Applications definition
THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    "django_extensions",
]

if security.DEBUG:
    THIRD_PARTY_APPS.append("silk")
    THIRD_PARTY_APPS.append("drf_yasg")

LOCAL_APPS = [
    "commands",
]

INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

# Routing Configuration
ROOT_URLCONF = "shakcommerce.urls"

WSGI_APPLICATION = "shakcommerce.wsgi.application"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGES = (
    ("en", "English"),
    ("ar", "Arabic"),
)
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Cairo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and Media files (CSS, JavaScript, Images, videos)
MEDIA_URL = "backend-media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
