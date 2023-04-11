from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_tienda import views
from api_tienda.views import StoreViewSet, BrandViewSet, DealViewSet, RegisterEndpoint, UserView, LoginView


router = DefaultRouter()
router.register(r'stores', views.StoreViewSet, basename="store")
router.register(r'brands', views.BrandViewSet, basename="brands")
router.register(r'deals', views.DealViewSet, basename="deals")

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterEndpoint.as_view(), name='register_endpoint'),
    path('users/', UserView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
]
