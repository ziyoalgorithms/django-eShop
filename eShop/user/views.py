from django.shortcuts import render


def user_main(request):
    return render(request, 'user/user_base.html')
