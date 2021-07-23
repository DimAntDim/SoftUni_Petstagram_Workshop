from accounts.forms import PetstagramUserLoginForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout


def user_login(request):
    if request.method == 'POST':
        form = PetstagramUserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = PetstagramUserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('landing page')