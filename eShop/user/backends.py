from django.db.models import Q

from user.models import UserAcc


class MultipleUsernameBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserAcc.objects.get(Q(email=username) | Q(
                phone=username) | Q(name=username))
            if user.check_password(password):
                return user
        except:
            UserAcc.set_password(password)
