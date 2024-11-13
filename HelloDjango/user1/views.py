from django.shortcuts import render, redirect
from .forms import UserRegForm, ProfilesImgForm, UserUpdateForm, TarifsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, CreateView
from .models import Profiles, User
from django.views.generic.edit import FormMixin

# Create your views here.

def register(request):
    if request.method  == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('profile')
    else:
        form = UserRegForm()
    return render(
        request,
        'user1/reg.html',
        {
            'title':'Страница регестации',
            'form':form
        })

@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfilesImgForm(request.POST,request.FILES, instance=request.user.profiles)
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        if profileForm.is_valid() and updateForm.is_valid():
            updateForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        profileForm = ProfilesImgForm(instance=request.user.profiles)
        updateForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm':profileForm,
        'updateForm':updateForm,
        'title':'Профиль пользователя'
    }
    return render(request, 'user1/profile.html', data)


def tarifs(request):
    if request.method == 'POST':
        tarifform = TarifsForm(request.POST,request.POST['ac_type'], instance=request.user.profiles)
        if tarifform.is_valid():
            tarifform.save()

            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('tarif')
    else:
        tarifform = TarifsForm()

    data = {
        'tarifform': TarifsForm,
        'title': 'Тарифы на сайте'
    }
    return render(request, 'user1/tarif.html', data)

