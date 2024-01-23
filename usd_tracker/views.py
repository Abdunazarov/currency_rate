from django.http import JsonResponse
from .models import ExchangeRate


def get_current_usd(request):
    last_rates = ExchangeRate.objects.only("rate", "timestamp").order_by("-timestamp")[
        :10
    ]
    current_rate = last_rates[0].rate if last_rates else None
    data = {
        "current_rate": current_rate,
        "last_requests": list(last_rates.values("rate", "timestamp")),
    }
    return JsonResponse(data)
