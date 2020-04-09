from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

GENDER_OPTIONS = [
    ('female', 'Female'),
    ('male', 'Male')
]


class User(PermissionsMixin, AbstractUser):
    "Django's permission framework gives you all the methods and db fields to support permission model"
    first_name = models.CharField(db_column="First Name", max_length=15)
    last_name = models.CharField(db_column="Last Name", max_length=30)
    gender = models.CharField(db_column="Gender", max_length=10, choices=GENDER_OPTIONS, default=GENDER_OPTIONS[0][0])
    address = models.CharField(db_column='Address', max_length=255, help_text="Flat No, Building, Street, Area")
    locality = models.CharField(db_column='Locality', max_length=20, help_text='Locality/Town')
    state = models.CharField(db_column='State', max_length=30)
    district = models.CharField(db_column='District', max_length=30)
    city = models.CharField(db_column='City', max_length=30, help_text="City or Taluka")
    pincode = models.CharField(db_column='Pincode', max_length=10, help_text="Pincode stored as Chars")

    phone_number = models.CharField(db_column="Phone Number", max_length=13, unique=True)

    # primary key of user
    email_id = models.EmailField(db_column="Email ID", max_length=40, unique=True, primary_key=True)

    password = models.CharField(db_column="Password", max_length=200)
    date_joined = models.DateTimeField(db_column="Date Joined", auto_now_add=True)

    USERNAME_FIELD = 'email_id'
    EMAIL_FIELD = 'email_id'
    # for createsuperuser command will prompt for following
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email_id', 'gender']

    is_active = models.BooleanField(
        db_column="Is Active",
        default=False,
        help_text=_(
            "Designates whether this user should be considered active or not."
        ),
    )

    # permissions for accessing admin page
    is_staff = models.BooleanField(
        _('is_staff'),
        db_column='Is Staff',
        default=False,
        help_text=_(
            'Designates whether this user is a member of staff to access the admin page or not'
        )
    )
    is_superuser = models.BooleanField(
        _('is_superuser'),
        db_column='Is Superuser',
        default=False,
        help_text=_(
            'Designates whether this user has all permissions in the admin page or not'
        )
    )

    # custom user model defining username field other than username should define Custom Model Manager
    # objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        "return the user name and phone number of user"
        return self.get_full_name() + ":" + self.get_username()

    def get_username(self):
        "Return the identifying username i.e. phone number for this user"
        return getattr(self, self.USERNAME_FIELD)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    # def get_absolute_url(self):
    #     return reverse('sign-up')

    @property
    def is_active_user(self):
        "Is the user active?"
        return self.is_active

    @property
    def is_staff_user(self):
        "Is user is member of staff?"
        return self.is_staff

    @property
    def is_super_user(self):
        "Is the user a superuser?"
        return self.is_superuser

    # access of the user to admin content: permissions
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        if self.is_staff or self.is_superuser:
            return True
        else:
            return False

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True