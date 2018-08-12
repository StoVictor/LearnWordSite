import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UniqueEmailField(EmailField):

    def validate(self, value):
        super().validate(value)
        try:
            User.objects.get(email = value)
            raise forms.ValidationError("Данная электронная почта уже зарегестрирована")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Данная электронная почта уже зарегестрирована")
        except User.DoesNotExist:
            pass

class RegisterForm(UserCreationForm):
    email = UniqueEmailField(label=_("Email address"), required=True,
        help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email")
