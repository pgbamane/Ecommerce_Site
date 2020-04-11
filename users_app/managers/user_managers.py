from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email_id, password=None, **extra_fields):
        email_id = self.normalize_email(email_id)
        user = self.model(phone_number=phone_number, email_id=email_id, **extra_fields)
        user.set_password(raw_password=password)
        user.save()
        return user

    def create_superuser(self, phone_number, email_id, password=None, **extra_fields):
        user = self.create_user(phone_number, email_id, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_staffuser(self, phone_number, email_id, password=None, **extra_fields):
        user = self.create_user(phone_number, email_id, password, **extra_fields)
        user.is_staff = True
        user.save()
        return user
