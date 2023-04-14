from django import forms
from django.forms import ModelForm
from .models import PartygamePost

class PartygamePostForm(ModelForm):
    class Meta:
        model = PartygamePost
        # フォームで使用するフィールド
        fields = ['category', 'category2', 'category3', 'category4', 'title', 'subtitle', 'item', 'preparation', 'wincondition', 'detail']

        widgets = {
            'item': forms.Textarea(attrs={'rows':4}),
            'preparation': forms.Textarea(attrs={'rows':4}),
            'detail': forms.Textarea(attrs={'rows':4}),
        }

class ContactForm(forms.Form):
    # フォームのフィールドをクラス変数として定義
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # フィールドの初期化
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '件名を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        