admin_init () {
  cat <<EOF
from .${app_name}_admin import *

EOF
}
