from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Measurement,Sensor
from .serializers import MeasurementSerializer,SensorDetailSerializer
from .serializers import SensorsSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action

#get - отображаем датчики 
#post - создаем датчик
#patch - обновление датчика
class SensorsView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

#post - добавление измерения.
class UpdateMeasureView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#get -получение информации по датчику
class SensorsDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
