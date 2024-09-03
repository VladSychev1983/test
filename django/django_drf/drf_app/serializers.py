from rest_framework import serializers
from drf_app.models import Weapon

#Ручной сереализатор. 
# class WeaponSerializer(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()

#встроенный в django
class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id','power','rarity','value']

