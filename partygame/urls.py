from django.urls import path
from . import views

app_name = 'partygame'

urlpatterns = [
    # partygameアプリへのアクセス→viewsモジュールのIndexView
    path('', views.IndexView.as_view(), name='index'),

    # 投稿ページへのアクセスはviewsモジュールのCreatePartygameView
    path('post/', views.CreatePartygameView.as_view(), name='post'),

    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessView
    path('post_done', views.PostSuccessView.as_view(), name='post_done'),

    # カテゴリ一覧ページ
    path('partygame/category/<int:category>', views.CategoryView.as_view(), name='partygame_category'),

    # カテゴリ2一覧ページ
    path('partygame/category2/<int:category2>', views.Category2View.as_view(), name='partygame_category2'),

    # カテゴリ3一覧ページ
    path('partygame/category3/<int:category3>', views.Category3View.as_view(), name='partygame_category3'),

    # カテゴリ4一覧ページ
    path('partygame/category4/<int:category4>', views.Category4View.as_view(), name='partygame_category4'),

    # ユーザーの投稿一覧
    path('user-list/<int:user>', views.UserListView.as_view(), name='user_list'),

    # 詳細ページ
    path('partygame-detail/<int:pk>', views.DetailView.as_view(), name='partygame_detail'),

    # マイページ
    path('mypage/', views.MypageView.as_view(), name='mypage'),

    # 削除ページ
    path('partygame/<int:pk>/delete/', views.PartygameDeleteView.as_view(), name='partygame_delete'),
]
