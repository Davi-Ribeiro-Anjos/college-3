from django.shortcuts import render


# class


def index(request):
    return render(request, "home/index.html")
