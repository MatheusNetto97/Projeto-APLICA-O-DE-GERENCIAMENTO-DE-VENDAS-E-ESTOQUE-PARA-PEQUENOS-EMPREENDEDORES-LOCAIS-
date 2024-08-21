# backend/app/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, SaleViewSet, UserRegisterView, ReportsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'register', UserRegisterView, basename='register')
router.register(r'reports', ReportsView, basename='reports')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
