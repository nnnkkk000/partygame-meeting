from django.contrib import admin

# Register your models here.

from .models import Category, Category2, Category3, Category4, PartygamePost

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class CategoryAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class Category2Admin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class Category3Admin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class Category4Admin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class PartygamePostAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory、CategoryAdminを登録
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにCategory、CategoryAdminを登録
admin.site.register(Category2, Category2Admin)

# Django管理サイトにCategory、CategoryAdminを登録
admin.site.register(Category3, Category3Admin)

# Django管理サイトにCategory、CategoryAdminを登録
admin.site.register(Category4, Category4Admin)

# Django管理サイトにPartygamePost、PartygamePostAdminを登録
admin.site.register(PartygamePost, PartygamePostAdmin)
