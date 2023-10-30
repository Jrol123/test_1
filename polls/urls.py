from django.urls import path

from . import views

"""
Список всех возможных адресов c этой позиции
"""
urlpatterns = [
    path("", views.index, name="index"),
]
