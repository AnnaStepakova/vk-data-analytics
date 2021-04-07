from django.urls import path
from . import views

app_name = 'report'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('update/', views.update_data, name='update'),
    path('progress/<str:task_id>', views.get_progress, name='progress'),
    path('status/<str:task_id>', views.progress_status, name='status'),
]