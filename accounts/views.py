from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def registration_view(request: HttpRequest) -> HttpResponse:
    """ユーザー登録（サインアップ）ビュー

    新規ユーザーの登録と、登録直後の自動ログインを処理する。

    - GET リクエスト:
        空のサインアップフォームを表示する。
    - POST リクエスト:
        フォーム入力を検証し、ユーザーを作成する。
        - 検証成功時:
            - ユーザーを保存
            - 入力されたパスワードで認証を実行
            - 認証成功ならログイン状態にし ``accounts:welcome_view`` へリダイレクト
            - 認証失敗ならフォームにエラーメッセージを追加して再表示
        - 検証失敗時:
            - エラー内容を含めてフォームを再表示する

    Args:
        request (HttpRequest): クライアントから送信された HTTP リクエスト

    Returns:
        HttpResponse: 
            - GET またはエラー時: フォームを含んだテンプレートの描画結果
            - 成功時: ``accounts:welcome_view`` へのリダイレクトレスポンス
    """
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # フォームのデータ検証
            raw_password = form.cleaned_data.get("password1")
            # USERNAME_FIELD が email なので、 username 引数に email を渡す
            user = authenticate(
                request,
                username=user.email,
                password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("accounts:welcome_view")
            else:
                # 認証失敗時の処理
                form.add_error(None, "ログイン処理に失敗しました。管理者にお問い合わせください。")
        # form.is_valid() が False の場合。
    # GET で呼び出された場合。
    # 共にテンプレートを呼び出す。
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/registration.html", {"form": form})


class CustomLoginView(LoginView):
    """
    カスタムログインビュー
    
    - `LoginView` を継承してログイン機能を提供する。
    - `template_name` でログインフォームのテンプレートを指定。
    - `redirect_authenticated_user = True` により、
      すでに認証済みのユーザーがアクセスした場合はログインページではなくリダイレクトされる。
    """
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """
    カスタムログアウトビュー

    - `LogoutView` を継承してログアウト機能を提供する。
    - `next_page` にリダイレクト先を指定。
      ログアウト後は `home` ページに遷移するよう設定されている。
    - `reverse_lazy` を使うことで、URL 解決を遅延させ、
      モジュール読み込み時に URLConf がまだロードされていない場合でも安全。
    """
    # reverse_lazy の戻り値は str 型なので mypy 互換
    next_page: str = str(reverse_lazy("home"))


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