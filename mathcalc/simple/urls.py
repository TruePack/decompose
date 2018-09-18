from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc),  # Home page call function which return form for entering number
    path('simple/', views.search)  # return answer (prime factors)
]