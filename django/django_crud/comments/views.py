from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serilizers import CommentSerializer
from .models import Comment

#если нужно описать в ручную действия
class CommentViewSet2(ViewSet):
    #выводит все объекты данного ресурса.
    def list(self,request):
        return Response({'status':'OK'})
    #смотреть конкретный объект
    def retrive(self,request):
        pass
    #для удаления объекта 
    def destroy(self,request):
        pass
    #для обновления объекта
    def update(self,request):
        pass
    #для создания объекта
    def create(self,request):
        pass

#все методы уже все встроены в ModelViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    

