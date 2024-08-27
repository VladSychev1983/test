from django.views.generic import ListView
from django.shortcuts import render
from .models import Student,Teacher


def students_list(request):
    template = 'school/students_list.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    students_obj = Student.objects.order_by(ordering)
    context = {
        'students': students_obj,
    }

    return render(request, template, context)
