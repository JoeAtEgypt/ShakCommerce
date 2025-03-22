from django.core.exceptions import ValidationError

allowed_extensions = [
    "jpg",
    "jpeg",
    "pdf",
    "txt",
    "png",
    "svg",
    "mpeg",
    "gif",
    "webm",
    "MOV",
    "mkv",
    "HEIC",
    "JPG",
    "PNG",
    "JPEG",
    "GIF",
    "SVG",
    "WEBP",
    "webp",
]

extension_error_message = "allowed format is :  'jpg', 'png', 'jpeg',  'gif','svg'... "

IMAGE_SIZE = 25


def file_size(value):
    limit = IMAGE_SIZE * 1024 * 1000
    if value.size > limit:
        raise ValidationError(
            f"File too large. Size should not exceed {IMAGE_SIZE} MiB."
        )


allowed_extensions_file = ["pdf", "PDF", "docx", "DOCX"]
extension_error_message_file = "allowed format is :  'pdf', 'docx'"

svg_allowed_extensions = [
    "svg",
    "SVG",
    "png",
    "PNG",
]
svg_error_message = "allowed format is :  'svg', 'png'"
