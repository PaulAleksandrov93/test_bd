from django.urls import path
from .views import getMinuteAggregate

urlpatterns = [
    path('get-minute-aggregate/', getMinuteAggregate, name='get-minute-aggregate'), 
]

"""
URL-пути для приложения API.

- get-minute-aggregate/ : Путь для получения агрегированных данных за минуту.
"""