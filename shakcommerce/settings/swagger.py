from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ShakCommerce API",
        default_version="v1",
        description="API documentation for ShakCommerce",
        terms_of_service="",
        contact=openapi.Contact(email="youssefaymanshaker@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
