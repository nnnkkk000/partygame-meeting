from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import PartygamePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PartygamePost
from django.views.generic import DetailView, DeleteView

# Create your views here.

# トップページ
class IndexView(ListView):
    # index.htmlをレンダリング
    template_name = 'index.html'
    # 投稿日時の降順で並び替え
    queryset = PartygamePost.objects.order_by('-posted_at')
    # 1ページに表示するレコード件数
    paginate_by = 9

# デコレータによりCreatePartygameViewへのアクセスをログインユーザーに限定
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクト
@method_decorator(login_required, name='dispatch')
class CreatePartygameView(CreateView):
    # PartygamePostFormをフォームクラスとして登録
    form_class = PartygamePostForm
    # レンダリングするテンプレート
    template_name = "post_partygame.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('partygame:post_done')

    # フォームバリデーションを通過したときに呼ばれるフォームデータの登録
    def form_valid(self, form):
        # POSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

# 投稿完了ページ
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

# カテゴリページ
class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # categoryテーブルのidを取得
        category_id = self.kwargs['category']
        # filter(フィールド名＝id)で絞り込み
        categories = PartygamePost.objects.filter(category=category_id).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return categories

# カテゴリページ2
class Category2View(ListView):
    template_name = 'index.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # category2テーブルのidを取得
        category2_id = self.kwargs['category2']
        # filter(フィールド名＝id)で絞り込み
        categories2 = PartygamePost.objects.filter(category2=category2_id).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return categories2


# カテゴリページ3
class Category3View(ListView):
    template_name = 'index.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # category3テーブルのidを取得
        category3_id = self.kwargs['category3']
        # filter(フィールド名＝id)で絞り込み
        categories3 = PartygamePost.objects.filter(category3=category3_id).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return categories3

# カテゴリページ
class Category4View(ListView):
    template_name = 'index.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # category4テーブルのidを取得
        category4_id = self.kwargs['category4']
        # filter(フィールド名＝id)で絞り込み
        categories4 = PartygamePost.objects.filter(category4=category4_id).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return categories4

# ユーザーの投稿一覧ページ
class UserListView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # userテーブルのidを取得
        user_id = self.kwargs['user']
        # filter(フィールド名＝id)で絞り込み
        user_list = PartygamePost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

# 詳細ページ
class DetailView(DetailView):
    template_name = 'detail.html'
    model = PartygamePost

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9

    # クエリを実行
    def get_queryset(self):
        # filter(userフィールド＝userオブジェクト)で絞り込み
        queryset = PartygamePost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class PartygameDeleteView(DeleteView):
    template_name = 'partygame_delete.html'
    model = PartygamePost
    # 削除完了後にマイページへリダイレクト
    success_url = reverse_lazy('partygame:mypage')

    # レコードの削除
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

