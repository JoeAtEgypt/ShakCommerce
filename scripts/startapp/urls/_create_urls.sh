create_urls () {
  cat <<EOF
from django.urls import path
from $app_name.views import ${app_name_class}API

urlpatterns = [
    path('', ${app_name_class}API.as_view(), name='${app_name}-api'),
]

EOF
}
