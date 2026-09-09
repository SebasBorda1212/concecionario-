from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/token/', CustomAuthToken.as_view(), name='api_token'),
]