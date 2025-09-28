from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """サインアップ用
    
    Attributes:
        password1 (str): 入力されたパスワード
        password2 (str): 確認用パスワード（password1 と一致する必要がある）
        model (Type[CustomUser]): フォームが操作するユーザーモデル
        fields (tuple[str]): フォームで扱うモデルフィールド ("email", "nickname")
    """

    class Meta(UserCreationForm.Meta): # type: ignore
        """メタ情報
        
        UserCreationForm.Meta を継承することで
        パスワードバリデーションやラベルなどを引き継ぎつつカスタマイズ可能。
        """

        model = CustomUser
        fields = ("email", "nickname")


class CustomUserChangeForm(UserChangeForm):
    """ユーザー更新用フォーム
    
    UserChangeForm はユーザー情報変更用のフォームで、管理画面や
    ユーザープロフィール編集画面で使用されます。

    Attributes:
        model (Type[CustomUser]): フォームが操作するユーザーモデル
        fields (tuple[str]): フォームで編集可能なモデルフィールド ("email", "nickname")
        password (str, optional): 現在のパスワード（変更対象の場合に使用）
    """
    
    class Meta: # type: ignore
        model = CustomUser
        fields = ("email", "nickname")


class CustomLoginForm(AuthenticationForm):
    """ログイン用フォーム
    
    AuthenticationForm はユーザー認証（ログイン）用のフォームで、
    ユーザー名とパスワードの入力欄を自動で用意してくれます。

    Attributes:
        username (str): ログインに使用する識別子。CustomUser ではメールアドレス
        password (str): ユーザーのパスワード
        model (Type[CustomUser]): フォームが認証に使用するユーザーモデル
    """

    # CustomUser の USERNAME_FIELD が email のため
    username = forms.EmailField(label="Email") 