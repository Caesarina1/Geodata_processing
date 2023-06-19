from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .utils import RoleChoice, UnitChoice


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    role = forms.ChoiceField(choices=RoleChoice.CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class CombatUnitPositionForm(forms.Form):
    your_unit = forms.ChoiceField(choices=UnitChoice.CHOICES)
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)
    comment = forms.CharField(widget=forms.Textarea)
