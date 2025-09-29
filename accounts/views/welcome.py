from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

@login_required
def welcome_view(request: HttpRequest) -> HttpResponse:
    """
    ログインユーザー向けのウェルカムページビュー

    - `@login_required` デコレータにより、認証されていないユーザーは
      ログインページへリダイレクトされる。
    - ログイン済みユーザーには "accounts/welcome.html" テンプレートを表示する。

    Args:
        request (HttpRequest): クライアントから送信された HTTP リクエスト

    Returns:
        HttpResponse: ウェルカムページをレンダリングしたレスポンス
    """
    return render(request, "accounts/welcome.html")