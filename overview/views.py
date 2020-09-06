from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
# from .forms import ArticleForm
# from .models import Article, Comment
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required

import pandas as pd 

@login_required(login_url="user:login")
def index(request):

    dataframe = [-0.2, -0.1, 0, 0.1, 0.4]
    context = {
        "dataframe" : dataframe
    }
    return render(request, "overview.html", context)

