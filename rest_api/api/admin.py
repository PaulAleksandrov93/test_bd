from django.contrib import admin
from .models import MinuteAggregate

admin.site.register(MinuteAggregate)
"""
Регистрация модели `MinuteAggregate` в админ-панели Django.

Это позволяет управлять (в данном случае только просматривать) данными этой модели через административный интерфейс Django.
"""