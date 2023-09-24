from rest_framework import serializers
from .models import MinuteAggregate

class MinuteAggregateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели MinuteAggregate.

    Attributes:
        minute (DateTimeField): Поле с датой и временем минуты.
        average_value (FloatField): Среднее значение.
    """

    class Meta:
        model = MinuteAggregate
        fields = ['minute', 'average_value']