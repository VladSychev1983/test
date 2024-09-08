
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import AdvViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('adv', AdvViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
