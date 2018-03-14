from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class TowEstimatorForm(forms.Form):
    city = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "City"
                    }))
    distance = forms.DecimalField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "distance in kms"
                    }))
    dollies = forms.BooleanField(required=False)








#from django.shortcuts import render, get_object_or_404
#from django.views.generic import DetailView

#from .models import TowDB
#from django import forms
#from django.contrib.auth import get_user_model
# Create your views here.
#class TowEstimate(forms.Form):
#    city = forms.CharField(widget=forms.TextInput(
#        attrs={
#        "class": "form-control",
#        "placeholder": "City"
#        }
#    ))
#    distance = forms.IntergerField(widget=forms.IntegerInput(attrs={"class": "form-control", "placeholder": "distance in kms"}))
#    )
