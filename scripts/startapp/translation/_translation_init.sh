translation_init () {
  cat <<EOF
from .${app_name}_translations import *
EOF
}
