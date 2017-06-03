from django.shortcuts import render

# Create your views here.


def travels(request):

        # add in trips for the user and trips added by other users for the two tables
    return render(request, 'travels/travels.html')


def destination(request, id):
    return render(request, 'travels/destination.html')


def add(request):
    return render(request, 'travels/add.html')


def create(request):
    pass


def join(request, id):
    pass
