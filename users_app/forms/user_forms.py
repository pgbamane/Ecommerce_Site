from allauth.account.forms import SignupForm as sign_up_form
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users_app.models import User


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         # fields = ('first_name', 'last_name', 'gender', 'address', 'locality', 'state', )
#         exclude = ('date_joined', 'is_active', 'is_staff', 'is_superuser')
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserCreationForm):
#         model = User
#         # fields = ('first_name', 'last_name', 'gender', 'address', 'locality', 'state', )
#         exclude = ('date_joined', 'is_active', 'is_staff', 'is_superuser')


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=15, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

    def signup(self, request, user):
        user = User()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'gender', 'address', 'locality', 'state', 'email_id', 'password')
    #     # exclude = ('date_joined', 'is_active', 'is_staff', 'is_superuser')

    # def save(self, request):
    #     user = super(SignUpForm, self).save(request)
    #     return user
