serializer_init () {
  cat <<EOF
from .${app_name}_serializers import ${app_name_class}Serializer

EOF
}
