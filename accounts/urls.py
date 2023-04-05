from django.urls import path

# viewsモジュール
from . import views

# viewsをauth_viewsとして使用
from django.contrib.auth import views as auth_views

app_name = 'accounts'

# URLパターン
urlpatterns = [
    # サインアップページのビュー
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # サインアップ完了ページのビュー
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    # ログインページのビュー
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # ログアウトページのビュー
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
