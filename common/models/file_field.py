from django.core.validators import FileExtensionValidator
from django.db import models

from common.validators.image_validators import (
    allowed_extensions_file,
    extension_error_message_file,
    file_size,
)


class FileField(models.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "validators": [
                    FileExtensionValidator(
                        allowed_extensions=allowed_extensions_file,
                        message=extension_error_message_file,
                    ),
                    file_size,
                ],
            }
        )
        super().__init__(*args, **kwargs)
