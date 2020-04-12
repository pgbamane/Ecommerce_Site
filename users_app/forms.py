from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        # fields = ('first_name', 'last_name', 'gender', 'address', 'locality', 'state', )
        exclude = ('date_joined', 'is_active', 'is_staff', 'is_superuser')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = User
        # fields = ('first_name', 'last_name', 'gender', 'address', 'locality', 'state', )
        exclude = ('date_joined', 'is_active', 'is_staff', 'is_superuser')
