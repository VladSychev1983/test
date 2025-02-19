from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import AdvertisementSerializer,UserSerializer
from advertisements.models import Advertisement
from django_filters import rest_framework as filters
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle,UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "destroy", "partial_update"]:
            return [IsAuthenticated(),IsOwnerOrReadOnly()]
        return []
