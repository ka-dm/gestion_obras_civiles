from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

   
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def index(request):
    return HttpResponse("Eh, eh epa colombia...")


def login_view(request):

    doc_externo=open('app/templates/base.html')
    plt=Template(doc_externo.read()) 
    doc_externo.close()

    ctx=Context()

    docuemento=plt.render(ctx)

    return HttpResponse(docuemento)


