from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


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