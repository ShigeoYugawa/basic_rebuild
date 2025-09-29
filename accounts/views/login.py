from django.contrib.auth.views import LoginView
from ..forms import CustomAuthenticationForm


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
    form_class = CustomAuthenticationForm