# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.models import Twitter_Streams
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.http import JsonResponse

@login_required(login_url="/login/") 
def pages(request):         # This function will match all the .html static files 
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template(load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def home(request): #This function will load the index.html particularly matching /
    context = {}
    try:
        
        html_template = loader.get_template( 'index.html' )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile(request): #This function will load the profile.html particularly matching /profile
    context = {}

    try:
        
        html_template = loader.get_template( 'profile.html' )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")       
def score_chart(request):
    labels = []
    data = []

    queryset = Twitter_Streams.objects.values().order_by('-created_at')[:10]
    for entry in queryset:
        labels.append(entry['created_at'].strftime("%H:%M:%S"))
        data.append(entry['compound_score'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

