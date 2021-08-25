from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Backend Activo",
      default_version='v1',
      description="Public Documentation Backend Activo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@activoeam.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    re_path('dev/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('dev/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('dev/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
