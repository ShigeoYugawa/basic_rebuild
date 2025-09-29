from __future__ import annotations
from typing import Any, Optional, TYPE_CHECKING
from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail
from django.views.generic.edit import FormView

if TYPE_CHECKING:
    from ..forms import CustomUserCreationForm

User = get_user_model()


class RedirectAuthenticatedMixin:
    """ログイン済ユーザーを特定ページへリダイレクト"""
    
    redirect_authenticated_url = "/"

    def dispatch(
        self, 
        request: HttpRequest, 
        *args: Any, 
        **kwargs: Any
    ) -> HttpResponse:
        if request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect(self.redirect_authenticated_url)
        return super().dispatch(request, *args, **kwargs)
    
class AutoLoginMixin:
    """フォーム保存後に自動ログイン"""

    def auto_login_user(
        self, 
        form: CustomUserCreationForm, 
        request: HttpRequest
    ) -> Optional[User]:
        user = form.save()
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(request, username=user.email, password=raw_password)
        if user:
            login(request, user)
            return user
        return None
    

class RegistrationEmailNotificationMixin:
    """ユーザー登録後にメール通知を送る"""
    email_subject = "ユーザー登録完了のお知らせ"
    email_message = "ユーザー登録が完了しました。"

    def send_registration_email(self, user: User) -> None:
        send_mail(
            self.email_subject,
            self.email_message,
            "noreply@example.com",
            [user.email],
            fail_silently=True,
        )


class RegistrationView(
    RedirectAuthenticatedMixin,
    AutoLoginMixin,
    RegistrationEmailNotificationMixin,
    FormView
):
    """ユーザー登録ビュー"""
    
    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        user = self.auto_login_user(form, self.request)
        if user:
            self.send_registration_email(user)
            return super().form_valid(form)
        else:
            form.add_error(None, "ログイン処理に失敗しました。")
            return self.form_invalid(form)