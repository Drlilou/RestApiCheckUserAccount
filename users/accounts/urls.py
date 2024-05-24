from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
]
