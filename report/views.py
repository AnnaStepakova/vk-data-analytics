from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import fill_db_tables


def index_view(request):
    return render(request, 'report/index.html', {})


def update_data(request):
    fill_db_tables()
    return HttpResponseRedirect(reverse('report:index'))
