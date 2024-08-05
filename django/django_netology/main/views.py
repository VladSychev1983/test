import datetime
from django.http import HttpResponse
from django.shortcuts import render,reverse
import os

def home_view(request):
    template_name = 'home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }   
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = []
    current_dir = os.getcwd()
    files_in_dir = os.listdir(current_dir)
    for file_name in files_in_dir:
        file_path = os.path.join(current_dir,file_name)
        print(file_path)
        files_list.append(file_path)
    files_string = "\n".join(files_list)
    return HttpResponse(files_string)