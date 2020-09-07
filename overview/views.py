from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
# from .forms import ArticleForm
# from .models import Article, Comment
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required

import pandas as pd 
from . import overview

@login_required(login_url="user:login")
def index(request):
    topics = ["football","covid", "BLM", "student", "online" ,"dog"]
    scores = overview.get_scores()
    
    day_wise_scores = overview.get_daywise_score()
    context = {}
    context['topics']  = topics
    context['scores'] = scores
    context['data'] = overview.formatted_data_for_chart(day_wise_scores)
    context['dates'] = overview.get_name_range_for_dates()
    context['range'] = range(0,6)
    return render(request, "overview.html", context)

