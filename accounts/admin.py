from django.contrib import admin

# Register your models here.

from .models import CustomUser

# 管理ページのレコード一覧に表示するカラム
class CustomUserAdmin(admin.ModelAdmin):

    # idとusernameを表示
    list_display = ('id', 'username')
    # カラムのリンク
    list_display_links = ('id', 'username')

# Django管理サイトにCustomUserとCustomUserAdminを登録
admin.site.register(CustomUser, CustomUserAdmin)
