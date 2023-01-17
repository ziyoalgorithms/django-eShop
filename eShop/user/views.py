from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, logout, authenticate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib import messages

from user.models import UserAcc
from user.forms import (
    RegistrationForm,
    UserLoginForm,
    UserEditForm,
    UserProfileEditForm,
)
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

    login_form = UserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else '/'

    if request.method == 'POST' and login_form.is_valid():

        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(next)

    context = {
        'form': login_form,
        'next': next,
    }

    return render(request, 'user/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def edit_user(request):

    if request.method == 'POST':
        edit_form = UserEditForm(
            request.POST,
            instance=request.user,
        )
        user_profile_form = UserProfileEditForm(
            request.POST,
            instance=request.user.profile,
        )

        if edit_form.is_valid() and user_profile_form.is_valid():
            edit_form.save()
            user_profile_form.save()
            messages.success(request, "Ma'lumotlaringiz tahrirlandi!")
            return HttpResponseRedirect('/users/dashboard/')

    else:
        edit_form = UserEditForm(instance=request.user)
        user_profile_form = UserProfileEditForm(instance=request.user.profile)

    context = {
        'edit_form': edit_form,
        'user_profile_form': user_profile_form,
    }

    return render(request, 'user/user_edit.html', context=context)


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')


@login_required
def user_delete(request):
    user = UserAcc.objects.get(email=request.user)
    user.is_active = False
    user.save()
    logout(request)
    messages.success(request, "Akkauntingiz o'chirildi")
    return redirect('/')
