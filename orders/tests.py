from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTestCase(TestCase):
    client = Client()
    response = client.get(reverse('orders:home'))

    def test_home_view_status(self):
        response = self.response
        self.assertEqual(response.status_code, 200)

    def test_home_to_order_link(self):
        response = self.response
        print(response)
        self.assertContains(response, '<a href="%s">' % reverse('orders:order'))


class OrderViewTestCase(TestCase):
    client = Client()
    response = client.get(reverse('orders:order'))

    def test_order_view_status(self):
        response = self.response
        self.assertEqual(response.status_code, 200)


class ReceiptViewTestCase(TestCase):
    client = Client()
    response = client.get(reverse('orders:receipt'))

    def test_receipt_view_status(self):
        response = self.response
        self.assertEqual(response.status_code, 200)
