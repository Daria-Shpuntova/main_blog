from django import forms
from .models import Application, Komment

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        help_text='Нельзя вводить символы: @,{,}',
        widget=forms.TextInput(attrs={'class': 'name_text', 'placeholder': 'Имя'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'phone_text', 'placeholder': 'Телефон'}))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'email_text', 'placeholder': 'Email'})
    )

    class Meta:
        model = Application
        fields = ['name', 'phone_number', 'email']


class CommentForm(forms.ModelForm):
    comment=forms.CharField(label='Текст комментария',required=True, widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = Komment
        fields = ['comment']