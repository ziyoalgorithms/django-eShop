from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, logout, authenticate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages

from user.models import UserAcc
from user.forms import RegistrationForm, UserLoginForm
from user.token import account_activation_token


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = 'Akkauntingizni faollashtiring'
            message = render_to_string('user/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            user.email_to_user(subject=subject, message=message)
            messages.success(
                request, "Tasdiqlovchi link elektron pochtangizga jo'natildi!")

    return render(request, 'user/registration.html', {'form': form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserAcc.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExists):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'user/activation_failed.html')


def login_user(request):

    form = UserLoginForm()
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        return redirect('user:login')

    context = {
        'form': form,
        'next': next,
    }

    return render(request, 'user/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('/')
