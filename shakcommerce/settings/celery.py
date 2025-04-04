import os

from shakcommerce.settings import TIME_ZONE

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_TIMEZONE = TIME_ZONE
## for the Result Backend
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379/0")
# CELERY_ACCEPT_CONTENT = ["application/json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"

CELERY_BEAT_SCHEDULE = {
    "test_celery_beat": {
        "task": "test_celery_beat",
        "schedule": 3.0,
        "args": (),
    },
}
