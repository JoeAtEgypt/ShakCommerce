create_translation () {
  cat <<EOF
from modeltranslation.translator import TranslationOptions, register
from $app_name.models import $app_name_class


class ${app_name_class}TranslationOptions(TranslationOptions):
    fields = (
        "name",
    )

EOF
}
