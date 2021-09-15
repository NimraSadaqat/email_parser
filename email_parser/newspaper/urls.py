from django.urls import path
from . import views

app_name = 'newspaper'

urlpatterns = [
    path('', views.index, name='main-view'),
    # path('', views.EmailView.as_view(), name='main-view'),
    # path('week/', views.WeekView.as_view(), name='weekcalendars'),
    # path('agenda/', views.AgendaListView.as_view(), name='agenda'),
]
