from django.urls import path
from .views import TransactionDataAPIView

urlpatterns = [
    path('get_transaction/', TransactionDataAPIView.as_view())
]
