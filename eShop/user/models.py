from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Emailingizni kiritishingiz kerak!")
        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()

        return user


class UserAcc(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'Users Accounts'

    def __str__(self):
        return self.email


GENDER_CHOICES = (
    ('ERKAK', 'Erkak'),
    ('AYOL', 'Ayol')
)

COUNTRY_CHOICES = (
    ('SAMARQAND', 'Samarqand'),
    ('JIZZAH', 'Jizzah'),
    ('SURXONDARYO', 'Surxondaryo'),
    ('QASHQADARYO', 'Qashqadaryo'),
    ('SIRDARYO', 'Sirdaryo'),
    ('TOSHKENT', 'Toshkent'),
    ('NAVOIY', 'Navoiy'),
    ('NAMANGAN', 'Namangan'),
    ('ANDIJON', 'Andijon'),
    ('FARGONA', "Farg'ona"),
    ('XORAZM', 'Xorazm'),
    ('NUKUS', 'Nukus'),
)


class UserAccProfile(models.Model):

    user = models.OneToOneField(
        UserAcc,
        db_index=True,
        related_name='profile',
        on_delete=models.PROTECT,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(
        upload_to='users_images/',
        default='users_images/default_user_image.png'
    )
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    country = models.CharField(max_length=12, choices=COUNTRY_CHOICES)
    address_line = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f"{self.first_name} {self.user.email}"
