from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shakcommerce import settings

api_patterns = []
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
        path(
            "swagger/",
            settings.schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            settings.schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
