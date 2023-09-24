from django.db import models


class MinuteAggregate(models.Model):
    """
    Модель для представления 'minute_aggregate_view'.

    Attributes:
        minute (DateTimeField): Поле с датой и временем минуты.
        average_value (FloatField): Среднее значение.
    """
    
    minute = models.DateTimeField(primary_key=True)
    average_value = models.FloatField()

    class Meta:
        managed = False  # Указываем, что эта модель не управляет созданием/удалением таблицы
        db_table = 'minute_aggregate_view'  # Указываем имя представления
