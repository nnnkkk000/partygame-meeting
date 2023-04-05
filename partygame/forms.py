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

