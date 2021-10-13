from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def login_view(request):

    doc_externo=get_template('base.html')
    docuemento=doc_externo.render({})

    return HttpResponse(docuemento)


