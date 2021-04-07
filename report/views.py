from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .tasks import process_posts
from celery.result import AsyncResult


def index_view(request):
    return render(request, 'report/index.html', {})


def update_data(request):
    result = process_posts.delay(days=14)
    print(result.backend)
    task_id = result.task_id
    return HttpResponseRedirect(reverse('report:progress', args=[str(task_id)]))


def get_progress(request, task_id):
    result = AsyncResult(id=task_id)
    return render(request, 'report/progress.html', {'state': result.state})
