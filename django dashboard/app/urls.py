# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.home, name='dashboard-home'),

    # The profile
    path('profile/', views.profile, name='dashboard-profile'),


    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

    #live score chart
    path('score-chart/', views.score_chart, name='score-chart'),

]
