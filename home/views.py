from django.shortcuts import render

# Create your views here.

def index(request):
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
    appStyle = "/home/css/homebase.css"
    appData.update({
        "activeApp": activeApp,
        "appStyle": appStyle,
        "loggedIn": loggedIn,
        "userId": userId,
        "baseHome": "home/baseHome.html",
        "colorPalette": colorPalette,
    })

    return render(request, "home/index.html", appData)