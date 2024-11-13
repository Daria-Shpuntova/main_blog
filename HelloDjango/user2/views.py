from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm, ProfilesImgForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.


def register(request):
    if request.method  == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('home')
    else:
        form = UserRegForm()
    return render(
        request,
        'user2/register.html',
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
        'updateForm':updateForm
    }
    return render(request, 'user2/profile.html', data)




