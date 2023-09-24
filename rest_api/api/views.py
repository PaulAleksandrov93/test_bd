from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MinuteAggregate
from .serializers import MinuteAggregateSerializer

from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMinuteAggregate(request):
    """
    Получаем агрегированные данные по минутам.

    Args:
        request (Request): Объект запроса.

    Returns:
        Response: Объект ответа с данными.
    """
    
    minute_aggregate_data = MinuteAggregate.objects.all()
    count = minute_aggregate_data.count()  # Получаем количество записей

    serializer = MinuteAggregateSerializer(minute_aggregate_data, many=True, context={'request': request})
    return Response({'count': count, 'data': serializer.data})