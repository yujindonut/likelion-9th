from django.contrib.auth.forms import UserCreationForm,UserChangeForm,get_user_model
from django.contrib.auth import get_user_model
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname','age', 'gender']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['nickname','gender','age']