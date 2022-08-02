from django.forms import ModelForm
from.models import profile
from django.contrib.auth.models import User

class profile_form(ModelForm):
    class Meta:
        model=profile
        fields =['image']

class user_form(ModelForm):
    class Meta:
        model=User
        fields =['username','email']

