from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from events.forms import RegisterForm, LoginForm, EventForm
from events.models import Event


def home(request):
    context = {}
    events = Event.objects.all().order_by('-start_date')
    context['events'] = events
    return render(request, 'events/home.html', context)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form = LoginForm()
        return render(request, 'events/login.html', {'form' : form})
    else:
        return redirect('/')


def user_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                account = authenticate(username=username, password=password)
                login(request, account)
                return redirect('/')
        else:
            form = RegisterForm()
        return render(request, 'events/register.html', {'form': form})
    else:
        return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')


def create_event(request):
    print(request)
    context = {}
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'events/event.html', {'form': form})
    else:
        form = EventForm()
    return render(request, 'events/event.html', {'form': form})


def like_event(request):
    event_id = request.POST.get('event_id')
    user = request.user

    event = get_object_or_404(Event, id=event_id)

    is_liked = False
    if event.likes.filter(id=user.id).exists():
        event.likes.remove(user)
        is_liked = False
    else:
        event.likes.add(user)
        is_liked = True

    return HttpResponseRedirect(reverse('event_detail', args=[str(event_id)]))


def like_view(request):
    context = {}
    is_liked = []
    if not request.user.is_authenticated:
        return redirect('/login')

    all_liked_events = Event.objects.filter(likes__id=request.user.id)
    context['all_liked_events'] = all_liked_events

    for liked in all_liked_events:
        is_liked.append(liked.id)
    context['is_liked'] = is_liked
    return render(request, 'events/liked_events.html', context)


def event_detail(request, pk):
    context = {}
    if not request.user.is_authenticated:
        return redirect('/login')

    event = Event.objects.get(id=pk)
    context['event'] = event

    stuff = get_object_or_404(Event, id=pk)
    context['total_likes'] = stuff.total_likes()

    is_liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        is_liked = True

    context['is_liked'] = is_liked
    return render(request, 'events/event_detail.html', context)
