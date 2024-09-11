from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import Adv
from app.serializers import AdvSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle

class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    #permission_classes = [IsOwnerOrReadOnly]
    #указать тротлинг для определнного вьюсета.
    throttle_classes = [AnonRateThrottle]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


