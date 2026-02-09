from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class CustomUser(AbstractUser):
    #Extra fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('client', 'Client'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username

#Staff OTP Model
class StaffOTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def generate_code(self):
        self.code = str(random.randind(100000, 999999))