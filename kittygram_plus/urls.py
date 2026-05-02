# kittygram_plus/urls.py
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet, basename='cat')
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcat')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
