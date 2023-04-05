from django.contrib.auth.forms import UserCreationForm

# models.pyのUserモデル
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # 連携するモデル＝CustomUser
        model = CustomUser
        # フォームで使用するフィールド：ユーザ名、メール、パスワード、パスワード確認用
        fields = ('username', 'email', 'password1', 'password2')

