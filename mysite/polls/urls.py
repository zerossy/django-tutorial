from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views.py 에서 정의한 index 함수
]