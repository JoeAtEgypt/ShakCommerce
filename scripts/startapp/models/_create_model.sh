create_model () {
  cat <<EOF
from django.db import models
from common.models import BaseModel, WEBPField
from common.validators.image_validators import (
    allowed_extensions,
    extension_error_message,
    file_size,
    allowed_extensions_file,
    extension_error_message_file,
)

class $app_name_class(BaseModel):
    name = models.CharField(max_length=255)
EOF
}
