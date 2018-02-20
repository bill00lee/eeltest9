from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from gettingstarted.forms import ContactForm



# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    context = {
        "title":"homepage",
        "content":"info about the homepage"
    }
    return render(request, 'index.html', context)

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
        "title":"Contact page",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
