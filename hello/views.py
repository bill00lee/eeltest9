from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Greeting
from gettingstarted.forms import ContactForm



# Create your views here.
def home_page(request):
    print(request.session.get("first_name", "Unknown"))
    # return HttpResponse('Hello from Python!')
    context = {
        "title":"homepage",
        "content":"info about the homepage",
            }
    if request.user.is_authenticated:
        context["premium_content"] = "Premium content section"
    return render(request, "home_page.html", context)

def about_page(request):
    # return HttpResponse('Hello from Python!')
    context = {
        "title":"about",
        "content":"info about the about"
    }
    return render(request, 'about_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)