from django.urls import path
from . import views

urlpatterns = [
    path("", views.calc)  # Factorization to prime factors.
]
