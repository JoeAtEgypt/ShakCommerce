model_init () {
  cat <<EOF
from .${app_name}_models import $app_name_class

EOF
}
