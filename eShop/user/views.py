from django.shortcuts import render, redirect

from user.models import UserAcc
from user.forms import RegistrationForm


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

    return render(request, 'user/registration.html')
