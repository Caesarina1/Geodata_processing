from django import forms
from geo_base import utils


class DataTransferForm(forms.Form):
    target_type = forms.ChoiceField(choices=utils.TargetChoice.CHOICES)
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=False)


class CombatUnitPositionForm(forms.Form):
    your_unit = forms.ChoiceField(choices=utils.UnitChoice.CHOICES)
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)
    comment = forms.CharField(widget=forms.Textarea)
