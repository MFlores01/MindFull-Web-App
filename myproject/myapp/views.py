# yourappname/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, traceback, logging
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
from .models import JournalEntry
from .forms import JournalEntryForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth






def index(request):
    return render(request, 'index.html')


#def login_view(request):
    #return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a different page after successful login
            return redirect('myapp:dashboard')  # Change 'dashboard' to the desired URL name or path for your dashboard page
        else:
            # Handle invalid login credentials
            # You can customize this part based on your requirements
            return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})

    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'Student/dashboard.html')

def dashboard_new_css(request):
    return render(request, 'static/css/new.css')

def dashboard_chat(request):
    return render(request, 'Student/chat.html')

def dashboard_calendar(request):
    return render(request, 'Student/calendar.html')

def error(request):
    return render(request, 'Student/dashboard.html')

def dashboard_home(request):
    return render(request, 'Student/home.html')

def dashboard_music(request):
    return render(request, 'Student/music.html')

def dashboard_moodtrack(request):
    return render(request, 'Student/statistics.html')

@login_required
def dashboard_journal(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user  # Assign the authenticated user directly
            new_entry.save()
            return redirect('myapp:journal')
    else:
        form = JournalEntryForm()

    # Fetch all journal entries from the database
    journal_entries = JournalEntry.objects.all()

    # Pass the journal_entries variable and the form to the template context
    context = {'journal_entries': journal_entries, 'form': form}

    # Render the template with the provided context
    return render(request, 'Student/journal.html', context)

def journal_entry(request, title):
    # Fetch the journal entry with the given title from your database
    entry = get_object_or_404(JournalEntry, title=title)

    # Render the journal entry template with the content
    return render(request, 'Student/journal_entry.html', {'entry': entry})

'''
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 != password2:
                return render(request, 'signup.html', {'form': form, 'error_message': 'Passwords do not match.'})

            user = form.save()
            # Log the user in
            login(request, user)
            # Redirect to a different page after successful registration
            return redirect('myapp:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
  '''

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'signup.html', {'form': form, 'error_message': 'Passwords do not match.'})

            user = form.save()
            # Log the user in
            login(request, user)
            # Redirect to a different page after successful registration
            return redirect('myapp:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form, 'error_message': ''})

@csrf_protect
def save_entry(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            title = data.get('title')
            text = data.get('text')

            # Get the CustomUser instance from the SimpleLazyObject
            custom_user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user

            # Create a new JournalEntry instance and save it to the database
            new_entry = JournalEntry.objects.create(title=title, content=text, author=custom_user.customuser)
            new_entry.save()

            # Redirect to the journal page after saving the entry
            return HttpResponseRedirect(reverse('Student/journal.html'))
        
    except Exception as e:
        # Log the exception details using Django's logging
        logging.exception('An error occurred while saving the journal entry')
        return JsonResponse({'error': str(e)}, status=500)
    
def get_entries(request):
    if request.method == 'GET':
        # Retrieve all entries from the database
        entries = JournalEntry.objects.all().values('id', 'title', 'content', 'date')
        return JsonResponse(list(entries), safe=False)
    
def authorize_spotify(request):
    sp_oauth = SpotifyOAuth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# views.py
''' 
def spotify_callback(request):
    sp_oauth = SpotifyOAuth()
    token_info = sp_oauth.get_access_token(request.GET['code'])
    access_token = token_info['access_token']
    
    # Use the access token to make Spotify API requests
    sp = spotipy.Spotify(auth=access_token)

    # Example: Get the current user's playlists
    playlists = sp.current_user_playlists()

    # You can add your logic to handle the Spotify API response

    return redirect('dashboard/music/')  # Redirect to your app's main page af
'''