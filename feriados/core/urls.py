from django.urls import path
from . import views

urlpatterns = [
    path('natal', views.natal),
    path('ano_novo', views.ano_novo)
]
