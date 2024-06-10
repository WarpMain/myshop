from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Аутентификация и вход в систему пользователя после регистрации
            authenticated_user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('accounts:profile_form')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_form(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid() and request.user.is_authenticated:
            profile = profile_form.save(commit=False)  # Сначала создаем профиль, не сохраняя его в базе данных
            profile.user = request.user  # Присваиваем текущего пользователя атрибуту user профиля
            profile.save()  # Сохраняем профиль
            return redirect('shop:product_list')
    else:
        profile_form = ProfileForm()
    return render(request, 'accounts/profile_form.html', {'profile_form': profile_form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
