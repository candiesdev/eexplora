from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landingViews(request):
    if "palette" in request.GET:
        colorPalette = "palette" + request.GET["palette"]
    else:
        colorPalette = "none"
        
    if request.user.is_authenticated:
        loggedIn = True
        userId = request.user
    else:
        loggedIn = False
        userId = ""

    appData = {}
    activeApp = True
    appStyle = "/landing/css/landingbase.css"
    prev = "/landing"
    boxTemplate = "./boxtemplate.html"
    appData.update({
        "activeApp": activeApp,
        "appStyle": appStyle,
        "loggedIn": loggedIn,
        "userId": userId,
        "colorPalette": colorPalette,
        "prev": prev,
        "boxTemplate": boxTemplate,
    })
    return render(request, "landing/landingindex.html", appData)