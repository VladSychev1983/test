from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from advertisements.models import Advertisement

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = filters.CharFilter(field_name="status")
    creator = filters.NumberFilter(field_name="creator")
    created_at = filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ['status','created_at','creator']