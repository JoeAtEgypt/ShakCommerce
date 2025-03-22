from django.core.exceptions import ValidationError

allowed_video_extensions = [
    "webm",
    "WEBM",
    "mkv",
    "MKV",
    "flv",
    "FLV",
    "vob",
    "VOB",
    "ogv",
    "ogg",
    "gif",
    "gifv",
    "mng",
    "MTS",
    "M2TS",
    "TS",
    "mov",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "rmvb",
    "viv",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
]

extension_error_message_video = "video extension is not valid."

VIDEO_SIZE = 50


def file_size_video(value):
    limit = VIDEO_SIZE * 1024 * 1000
    if value.size > limit:
        raise ValidationError(
            f"File too large. Size should not exceed {VIDEO_SIZE} MiB."
        )
