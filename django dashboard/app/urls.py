# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.home, name='home'),

    # The profile
    path('profile/', views.profile, name='dashboard-profile'),


    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

    #live score chart
    path('score-chart/', views.score_chart, name='score-chart'),

    #day avg chart
    path('daily-avg/', views.daily_avg, name='daily-avg'),

    #total average chart
    path('total-avg/', views.total_avg, name='total-avg-chart'),

    #total score chart
    path('total-count/', views.total_count, name='total-count-chart'),

    #tweets text
    path('tweet-text/', views.get_tweets, name='tweet-text'),

]
