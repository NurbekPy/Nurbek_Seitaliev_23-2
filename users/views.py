from django.shortcuts import render, redirect
from users.forms import Loginform
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request):
    if request.method == 'GET':
        context = {
            'form': Loginform
        }
        return render(request, 'users/login.html', context=context)

    if request.method == 'POST':
        form = Loginform(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('/posts/')
            else:
                form.add_error('username', 'bad request')

        return render(request, 'users/login.html', context={
            'form': form
        })





