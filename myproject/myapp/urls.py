from django.urls import path
from .views import index
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/new.css', views.dashboard_new_css, name='new'),
    path('dashboard/journal/', views.dashboard_journal, name='journal'),
    path('dashboard/journal/<str:title>/', views.journal_entry, name='journal_entry'),
    path('dashboard/save_entry/', views.save_entry, name='save_entry'),
    path('dashboard/get_entries/', views.get_entries, name='get_entries'),
    path('dashboard/calendar/', views.dashboard_calendar, name='appoinment'),
    path('dashboard/chat/', views.dashboard_chat, name='chat'),
    path('dashboard/home/', views.dashboard_home, name='home'),
    path('dashboard/analysis/', views.dashboard_moodtrack, name='mood'),
    path('dashboard/music/', views.dashboard_music, name='music'),
    path('dashboard/journal/error', views.error, name='error'),
    path('authorize_spotify/', views.authorize_spotify, name='authorize_spotify'),
]
