from django.urls import path
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', BookViewSet, basename='api')
urlpatterns = router.urls

