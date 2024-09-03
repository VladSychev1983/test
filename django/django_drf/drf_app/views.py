from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from .models import Weapon
from .serializers import WeaponSerializer

from rest_framework import viewsets

# @api_view(['GET','POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#     #data = { 'message' : 'ok'}
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})

# Разделяем GET и POST  запросы  помощью встроенного метода APIView 
# class DemoView(APIView):
#     def get(self,request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)

#     def post(self,request):
#         return Response({'status': 'OK'})

class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self,request):
        return Response({'status': 'OK'})

#информация по одному конкретному оружию.
class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class NewView(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    #http_method_names = ['post']

