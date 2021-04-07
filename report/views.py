import vk
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .tasks import process_posts
from vkdataanalytics.settings import ACCESS_TOKEN


def index_view(request):
    return render(request, 'report/index.html', {})


def update_data(request):
    process_posts.delay(days=14)
    return HttpResponseRedirect(reverse('report:index'))
