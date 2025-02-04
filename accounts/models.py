from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # exclude fields from AbstractUser
    date_joined = None
    last_login = None
    email = None

    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
    )
    ROLE = (
        ("ADMIN", "ADMIN"),
        ("USER", "USER"),
    )
    ACCOUNT_STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE"),
    )
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True, choices=ROLE)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    current_location = models.CharField(max_length=155, blank=True, null=True)
    account_status = models.CharField(
        max_length=150, blank=True, null=True, choices=ACCOUNT_STATUS
    )
    is_premium = models.BooleanField(default=False, null=False, blank=True) 
    profile_picture = models.ImageField(
        upload_to="user_profile_pictures", blank=True, null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
