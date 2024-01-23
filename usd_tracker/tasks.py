from celery import shared_task
from .models import ExchangeRate
import requests
from django.utils.timezone import now
from currency_rate.settings import CURRENCY_API


@shared_task
def fetch_usd_rate():
    response = requests.get(CURRENCY_API)
    data = response.json()

    if response.status_code == 200 and "RUB" in data["conversion_rates"]:
        usd_to_rub_rate = data["conversion_rates"]["RUB"]
        ExchangeRate.objects.create(rate=usd_to_rub_rate, timestamp=now())
    else:
        print(f"Error fetching data: {data}")
