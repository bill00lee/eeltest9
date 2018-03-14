from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from towguideline.forms import TowEstimatorForm

#rom django import forms
#from django.contrib.auth import get_user_model
# Create your views here.
#from .models import TowDB
#from .forms import towestimatorform

def TowEstimatorView(request):
    tow_estimator_form = TowEstimatorForm(request.POST or None)
    context = {
        "title":"Tow Estimator",
        "content":" Welcome to the estimator page.",
        "form": tow_estimator_form ,
    }
    if tow_estimator_form .is_valid():
        print(tow_estimator_form .cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "towguideline/towestimator.html", context)
