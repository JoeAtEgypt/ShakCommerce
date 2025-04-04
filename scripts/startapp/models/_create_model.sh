create_model () {
  cat <<EOF
from django.db import models

class $app_name_class(models.Model):
    name = models.CharField(max_length=255)
EOF
}
