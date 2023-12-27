from django.urls import path
from journal import views

app_name = 'journal'
urlpatterns = [

    path('entry/create/', views.diary_entry_create, name='diary_entry_create'),
    path('entry/<str:date_entry>/', views.diary_entry_detail, name='diary_entry_detail'),
    path('mood/statistics/<str:start_date>/<str:end_date>/', views.mood_statistics, name='mood_statistics'),
]