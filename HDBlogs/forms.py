from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User # Telling django to create form based on User model
        fields = ('email', 'username', 'password1', 'password2') # in django password1 => password and password2 => confirm password
        