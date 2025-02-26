from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet

router = DefaultRouter()
router.register('comments',CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
