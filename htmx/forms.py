# Import UserCreationForm class from django.contrib.auth.forms module
from django.contrib.auth.forms import UserCreationForm
# Import User model from the current application's models module
from .models import User


class RegisterForm(UserCreationForm):
    """
    This class will extend UserCreationForm to provide registration fields 
    for User model
    """
    class Meta:
        """
        Meta class to specify the model and fields to be used in the form.
        """

        # Specify the model to be used by the form
        model = User
        # List of fields to include in the form
        fields = ["username", "password1", "password2"]
