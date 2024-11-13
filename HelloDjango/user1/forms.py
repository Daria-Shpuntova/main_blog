from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profiles

class UserRegForm(UserCreationForm):
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @,{,}',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите email'})
    )
 #   some=forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @,{,}',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )


    class Meta:
        model = User
        fields = ['email', 'username']


class ProfilesImgForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profiles
        fields = ['img']


class TarifsForm(forms.ModelForm):
    TYPE_CHOS = (
        ('Полный пакет', 'full'),
        ('Бесплатный пакет', 'free')
    )

    ac_type = forms.TypedChoiceField(choices = TYPE_CHOS)

    class Meta:
        model = Profiles
        fields = ['ac_type']