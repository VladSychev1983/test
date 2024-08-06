import datetime
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,reverse
from django.core.paginator import Paginator
import os

#свой контвертор path
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, self.format)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)

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

def hello(request):
    # Method GET it is DICT to send varables.
    #name = request.GET["name"] 
    name = request.GET.get("name")
    age = int(request.GET.get("age", 20))
    print(age)
    return HttpResponse(f"Привет! {name}")

def sum(request, a ,b):
    # Method URL передача параметров.
    result = a + b
    return HttpResponse(f"Sum = {result}")

def user_report(request, id: int, dt: datetime):
    return HttpResponse(f"Id: {id} date:{dt}")

CONTENT = [str(i) for i in range(10000)]
def pagi(request):
    page_number = request.GET.get("page", 1)
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page' : page
    }
    return render(request, 'pagi.html', context)