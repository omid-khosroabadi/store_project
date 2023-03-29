from django.test import TestCase
from django.urls import reverse


class TestOrders(TestCase):
    def setUp(self):
        pass

    def test_order_list_url(self):
        response = self.client.get('/order/')
        return self.assertEqual(response.status_code, 302)

    def test_order_list_name(self):
        response = self.client.get(reverse('orders:order_list'))
        return self.assertEqual(response.status_code, 302)

