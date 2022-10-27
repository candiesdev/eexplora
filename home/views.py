from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        loggedIn = True
        userId = request.user
    else:
        loggedIn = False
        userId = ""
    return render(request, "home/index.html", {"loggedIn": loggedIn, "userId": userId, "baseHome": "home/baseHome.html"})