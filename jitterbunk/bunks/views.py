'''
/jitterbunk/bunks/views.py
This file contains the views related to bunking and viewing bunks.
This is the main view file.
'''
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Bunk


# MAIN BUNK FEED - Shows the user the most recent 5 bunks made on the app
def index(request):
    user = request.user
    latest_bunk_list = Bunk.objects.order_by('-time')[:5]

    # There's a problem with this somewhere - currently always returns False.
    # Meant for an extension to logging out
    if request.user.is_authenticated:
        logged_in = True;
    else:
        logged_in = False;

    context = {'latest_bunk_list': latest_bunk_list, 'logged_in' : logged_in}
    return render(request, 'bunks/index.html', context)

# SINGLE USER BUNK FEED - links to a user's own bunk feed, which shows them
# the bunks the specified user has received and given.
def main(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        from_user_bunk_list = Bunk.objects.filter(from_user_id=user_id)
        to_user_bunk_list = Bunk.objects.filter(to_user_id=user_id)
        user_list = User.objects
        context = {'page_on' : True, 'from_user_bunk_list': from_user_bunk_list,
         'to_user_bunk_list' : to_user_bunk_list, 'user_list' : user_list,
         'user' : user}

    except User.DoesNotExist:
        context = {'page_on' : False}

    return render(request, 'bunks/main.html', context)

# PAGE TO BUNK SOMEONE - allows the user to bunk the person by looking at
# someone else's profile
@login_required(login_url='/login')
def bunk(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    user = User.objects.get(id=user_id)

    from_user = request.user
    bunk = Bunk(from_user=from_user, to_user=to_user)
    bunk.save()
    from_user_bunk_list = Bunk.objects.filter(from_user_id=user_id)
    to_user_bunk_list = Bunk.objects.filter(to_user_id=user_id)
    user_list = User.objects
    context = {'page_on' : True, 'from_user_bunk_list': from_user_bunk_list, 'to_user_bunk_list' : to_user_bunk_list, 'user_list' : user_list, 'user' : user}
    return render(request, 'bunks/main.html', context)
