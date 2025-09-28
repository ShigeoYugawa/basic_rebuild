from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """CustomUser用の管理画面
    
    Django 管理サイトで CustomUser モデルを操作するための設定をまとめたクラス。

    Attributes:
        add_form (CustomUserCreationForm): 管理画面でユーザー新規作成時に使用するフォーム
        form (CustomUserChangeForm): 管理画面でユーザー編集時に使用するフォーム
        model (CustomUser): この管理クラスが対象とするユーザーモデル
        list_display (tuple[str]): 一覧画面に表示するフィールド
        list_filter (tuple[str]): 一覧画面で使用可能なフィルター
        search_fields (tuple[str]): 検索対象とするフィールド
        ordering (tuple[str]): 一覧画面でのデフォルト並び順
        fieldsets (tuple[tuple]): 管理画面のユーザー編集フォームで表示するフィールド構成
        add_fieldsets (tuple[tuple]): 管理画面でユーザー追加フォームを表示する際のフィールド構成
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("email", "nickname", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "nickname")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "nickname", "password")}),
        ("権限情報", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("重要な日付", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nickname", "password1", "password2", "is_staff", "is_active")}),
    )
