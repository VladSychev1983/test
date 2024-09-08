from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import Adv
from app.serializers import AdvSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsOwnerOrReadOnly

class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


