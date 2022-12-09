from django.contrib import admin
from django.urls import path, include
import booking

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('booking.urls'), name='booking'),
    path('', include('cinema.urls'), name='cinema'),
    path('', include('user.urls'), name='user'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            template_name='swagger-ui.html', url_name='schema'
        ),
        name='swagger-ui',
    ),
]