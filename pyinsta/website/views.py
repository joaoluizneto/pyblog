from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'website/index.html', context)

def detail(request, post_id):
    post = Post.objects.order_by('-pub_date')[:5]
    context = {'post': post}
    return render(request, 'website/index.html', context)