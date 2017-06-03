from django.shortcuts import render

# Create your views here.


def travels(request):
    return render(request, 'travels/travels.html')


def destination(request, id):
    return render(request, 'travels/destination.html')


def add(request):
    return render(request, 'travels/add.html')


def create(request):
    pass


def join(request, id):
    pass
