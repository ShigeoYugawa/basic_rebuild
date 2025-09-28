"""
アプリ全般の追加設定
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AccountsConfig(AppConfig):

    # pkが未指定の場合はidフィールドを64bitで自動生成する
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 管理画面でのアプリ名を日本語化する
    name = 'accounts'
    verbose_name = _("アカウント管理")