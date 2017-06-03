from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Plan
from ..log_reg.models import User

# Create your views here.


def travels(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "trips": Plan.objects.all(),
        "my_trips": Plan.objects.filter(creator=User.objects.get(id=request.session['user_id'])),
        "others_trips": Plan.objects.exclude(creator=User.objects.get(id=request.session['user_id']))
    }

    # add in trips for the user and trips added by other users for the two tables
    return render(request, 'travels/travels.html', context)


def destination(request, id):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('login:main')
    context = {
        "trip_deets": Plan.objects.filter(id=id),
        "joiners": Plan.objects.filter(joiners=id)
    }
    return render(request, 'travels/destination.html', context)


def add(request):
    return render(request, 'travels/add.html')


def create(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            response_from_models = Plan.objects.create_trip(
                int(request.session['user_id']), request.POST)
            if not response_from_models['status']:
                for error in response_from_models['errors']:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('travels:add')
            else:
                messages.add_message(request, messages.SUCCESS, "Trip has been added!")
                # redirect to travels:dashboard
    return redirect(reverse('travels:dashboard'))


def join(request, id, trip_id):
    response_from_models = Plan.objects.join_trip(id, trip_id)
    if response_from_models:
        messages.add_message(request, messages.SUCCESS,
                             "The trip has been added to your trips!")
    else:
        for error in response_from_models['errors']:
            messages.add_message(request, messages.ERROR, error)
    return redirect('travels:dashboard')
