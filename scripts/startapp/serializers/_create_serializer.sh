create_serializer () {
  cat <<EOF
from rest_framework import serializers
from $app_name.models import $app_name_class


class ${app_name_class}Serializer(serializers.Serializer):
    name = serializers.CharField()

EOF
}
