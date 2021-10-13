from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import Template, Context
#from django.template.loader import get_template


def login_view(request):
    return render(request, 'accounts/login.html', {})

def index(request):
    return render(request, 'button.html', {})
