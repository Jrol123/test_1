from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Возвращает страницу.

    index — внутреннее название страницы (?)

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the polls index.")
