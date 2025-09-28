from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    """ログアウト後や未ログイン時に表示するページ"""
    return render(request, "home.html")