from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    context = {
        "title":"title i inserted"
    }
    return render(request, 'index.html', context)

def about_page(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'about_page.html')

def contact_page(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'contact/views.html')

    if request.method == "POST":
         print(request.POST)
         print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
