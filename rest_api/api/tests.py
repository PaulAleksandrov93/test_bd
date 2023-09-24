from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

        
class MinuteAggregateTests(APITestCase):

    def setUp(self):
        # Создаем тестовые данные, если необходимо
        self.user = User.objects.create_user(username='testuser', password='test123!')

    # def test_get_minute_aggregate_authenticated(self):
    #     url = reverse('get-minute-aggregate')
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #     # Проверяем, что запрос завершился успешно (код 200)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Проверяем, что ответ содержит ожидаемые данные
    #     self.assertIn('count', response.data)
    #     self.assertIn('data', response.data)

    #     # Проверяем, что в ответе есть необходимые поля
    #     self.assertIn('minute', response.data['data'][0])
    #     self.assertIn('average_value', response.data['data'][0])
    
    def test_unauthorized_access(self):
        url = reverse('get-minute-aggregate')  

        response = self.client.get(url)

        # Проверяем, что запрос завершился с ошибкой аутентификации (код 403)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
