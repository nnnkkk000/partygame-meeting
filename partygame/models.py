from django.db import models

# Create your models here.

# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

# カテゴリを管理するモデル
class Category(models.Model):
    # カテゴリ名
    title = models.CharField(
        verbose_name='カテゴリ',    # フィールドのタイトル
        max_length=20
    )
    # オブジェクトを文字列にして返す
    def __str__(self):
        return self.title

# カテゴリを管理するモデル2
class Category2(models.Model):
    # カテゴリ名
    title = models.CharField(
        verbose_name='カテゴリ',    # フィールドのタイトル
        max_length=20
    )
    # オブジェクトを文字列にして返す
    def __str__(self):
        return self.title

# カテゴリを管理するモデル3
class Category3(models.Model):
    # カテゴリ名
    title = models.CharField(
        verbose_name='カテゴリ',    # フィールドのタイトル
        max_length=20
    )
    # オブジェクトを文字列にして返す
    def __str__(self):
        return self.title

# カテゴリを管理するモデル4
class Category4(models.Model):
    # カテゴリ名
    title = models.CharField(
        verbose_name='カテゴリ',    # フィールドのタイトル
        max_length=20
    )
    # オブジェクトを文字列にして返す
    def __str__(self):
        return self.title

# 投稿されたデータを管理するモデル
class PartygamePost(models.Model):
    # CustomUserモデルのuser_idとPartygamePostモデルを結びつける
    # CustomUserモデルが親でPartygamePostモデルが子
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        # ユーザーを削除する場合は投稿データも全て削除する
        on_delete=models.CASCADE
    )
    # CategoryモデルのtitleとPartygamePostを結びつける
    # Categoryモデルが親でPartygamePostモデルが子
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        # カテゴリに関連する投稿データが存在する場合はそのカテゴリを削除できない
        on_delete=models.PROTECT
    )
    # Category2モデルのtitleとPartygamePostを結びつける
    # Category2モデルが親でPartygamePostモデルが子
    category2 = models.ForeignKey(
        Category2,
        verbose_name='カテゴリ2',
        # カテゴリに関連する投稿データが存在する場合はそのカテゴリを削除できない
        on_delete=models.PROTECT
    )
    # Category3モデルのtitleとPartygamePostを結びつける
    # Category3モデルが親でPartygamePostモデルが子
    category3 = models.ForeignKey(
        Category3,
        verbose_name='カテゴリ3',
        # カテゴリに関連する投稿データが存在する場合はそのカテゴリを削除できない
        on_delete=models.PROTECT
    )
    # Category4モデルのtitleとPartygamePostを結びつける
    # Category4モデルが親でPartygamePostモデルが子
    category4 = models.ForeignKey(
        Category4,
        verbose_name='カテゴリ4',
        # カテゴリに関連する投稿データが存在する場合はそのカテゴリを削除できない
        on_delete=models.PROTECT
    )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=20
    )
    # サブタイトル用のフィールド
    subtitle = models.CharField(
        verbose_name='サブタイトル',
        max_length=50
    )
    # 必要アイテムのフィールド
    item = models.TextField(
        verbose_name='ゲームに必要なアイテム'
    )
    # 開始前準備のフィールド
    preparation = models.TextField(
        verbose_name='開始前の準備'
    )
    # 勝利条件のフィールド
    wincondition = models.CharField(
        verbose_name='勝利条件を一言で',
        max_length=100
    )
    # 詳細説明用のフィールド
    detail = models.TextField(
        verbose_name='詳細説明'
    )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        # 日時を自動で追加
        auto_now_add=True
    )

    # オブジェクトを文字列にして返す
    def __str__(self):
        return self.title

