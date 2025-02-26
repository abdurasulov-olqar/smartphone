from django.urls import path
from .views import (
    phone,
    get_by_ram,
    get_by_price_in_range,
)

urlpatterns = [
    path('smartphones/<int:id>', phone),
    path('smartphones/', phone),
    path('get-by-ram/', get_by_ram),
    path('get-by-price-range', get_by_price_in_range)
]
