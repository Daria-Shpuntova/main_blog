from django import forms
from .models import Komment2

class CommentForm(forms.ModelForm):
    comment=forms.CharField(label='Текст комментария',required=True, widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = Komment2
        fields = ['comment']
