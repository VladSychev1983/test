from django.http import HttpResponse
from django.shortcuts import render
from main.models import Car,Person
import random

def create_car(request):
    car = Car(brand=random.choice(['B1','B2','B3']),
              model=random.choice(['M1','M2','M3']),  
              color=random.choice(['C1','C2','C3']))
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand} {car.model}')

def list_car(request):
    #забрать все данные из базы
    car_objects = Car.objects.all()
    #фильтрация по полям.
    #car_objects = Car.objects.filter(brand='B3')
    #фитрация по содержанию полей.аналог like , вывести поле brand где есть 3 (модификаторы полей)
    #car_objects = Car.objects.filter(brand__contains='3')
    #отфильтровать по перому символу в таблице.
    #car_objects = Car.objects.filter(brand__startswith='2')
    cars = [f'{c.id} {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        #Person(name='P', car=car).save()
        #или
        Person.objects.create(name='Р', car=car)
    return HttpResponse('Все получилось!')

def list_person(request):
    person_objects = Person.objects.all()
    people = []
    people = [f'{p.name}: {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))