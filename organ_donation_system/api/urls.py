# api/urls.py
from django.urls import path
from .views import (
    DonorListCreateView, DonorRetrieveUpdateDestroyView,
    RecipientListCreateView, RecipientRetrieveUpdateDestroyView
)

urlpatterns = [
    # Donor endpoints
    path('donors/', DonorListCreateView.as_view(), name='donor-list-create'),
    path('donors/<int:pk>/', DonorRetrieveUpdateDestroyView.as_view(), name='donor-detail'),

    # Recipient endpoints
    path('recipients/', RecipientListCreateView.as_view(), name='recipient-list-create'),
    path('recipients/<int:pk>/', RecipientRetrieveUpdateDestroyView.as_view(), name='recipient-detail'),
]
