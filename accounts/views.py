from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# サインアップページのビュー
class SignUpView(CreateView):
    # forms.pyで定義したフォーム
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート＝signup.html
    template_name = 'signup.html'
    # サインアップ完了後のリダイレクト先＝accounts:signup_success
    success_url = reverse_lazy('accounts:signup_success')

    # フォームのバリデーションを通過した時に呼ばれるフォームデータの登録
    def form_valid(self, form):
        # formオブジェクトのフィールド値をデータベースに保存
        user = form.save()
        self.object = user
        return super().form_valid(form)

# サインアップ完了ページのビュー
class SignUpSuccessView(TemplateView):
    # レンダリングするテンプレート＝signup_success.html
    template_name = 'signup_success.html'
