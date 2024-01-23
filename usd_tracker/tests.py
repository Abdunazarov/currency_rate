from django.test import TestCase, Client
from django.urls import reverse
from .models import ExchangeRate
from django.utils.timezone import now


class ExchangeRateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("get-current-usd")
        ExchangeRate.objects.bulk_create(
            [
                ExchangeRate(rate=75.5, timestamp=now()),
                ExchangeRate(rate=76.0, timestamp=now()),
            ]
        )

    def test_current_usd_rate_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data["last_requests"]), 2)
        self.assertEqual(data["last_requests"][0]["rate"], 76.0)
        self.assertEqual(data["last_requests"][1]["rate"], 75.5)

    def test_current_usd_rate_no_data(self):
        ExchangeRate.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsNone(data["current_rate"])
        self.assertEqual(len(data["last_requests"]), 0)
