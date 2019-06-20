from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def books(request):
    return render(request, 'books.html')


def activity(request):
    return render(request, 'activity.html')


def wanted(request):
    return render(request, 'wanted.html')


def settings(request):
    return render(request, 'settings.html')


def system(request):
    return render(request, 'system.html')