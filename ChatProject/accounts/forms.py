from django.forms import ModelForm
from . import models

class CreateUserForm(ModelForm):
    class Meta:
        model = models.CustomUserModel
        fields = ['username', 'email', 'password']