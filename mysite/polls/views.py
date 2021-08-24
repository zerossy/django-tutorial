from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):  # $ python manage.py runserver 시  http://localhost:8000/polls/ 에서 보일 내용
    return HttpResponse("Hello, sydney. You're at the polls index if you want.")