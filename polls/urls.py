from django.urls import include, path

from . import views

"""
Список всех возможных адресов c этой позиции
"""
urlpatterns = [
    path("", views.index, name="index"),
]
