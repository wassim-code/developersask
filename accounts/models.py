from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email.')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password, is_staff=True, is_admin=True) 
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    username = models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_staff = models.BooleanField(default=False, verbose_name='staff')
    is_admin = models.BooleanField(default=False, verbose_name='admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def email_user(subject, msg, form_email, **kwargs):
        send_mail(subject, msg, from_email, [self.email], **kwargs)
    
    def has_at_least_one_order(self):
        return self.order_set.all().count() >= 1