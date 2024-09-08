
from rest_framework import serializers
from app.models import Adv

class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = "__all__"
        read_only_fields = ['user']
