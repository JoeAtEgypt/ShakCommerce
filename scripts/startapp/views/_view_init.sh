view_init () {
  cat <<EOF
from .${app_name}_views import ${app_name_class}API

EOF
}
