from django.contrib.auth.forms import UserCreationForm,UserChangeForm,get_user_model
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','password1','password2','birthDay','gender','location']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['birthDay', 'gender', 'location']