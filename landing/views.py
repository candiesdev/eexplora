from django.shortcuts import render
from django.http import HttpResponse
from .contentData import landing, property, agent

# Create your views here.

def landingViews(request):

    if "lanId" in request.GET:
        lanId = request.GET["lanId"]
    else:
        lanId = "000"
    
    landingData = landing(lanId)
    propertyData = property(landingData["propertyId"])
    agentData = agent(landingData["agentId"])

    colorPalette = "paletteBS"
        
    if request.user.is_authenticated:
        loggedIn = True
        userId = request.user
    else:
        loggedIn = False
        userId = ""

    appData = {}
    activeApp = True
    appStyle = "/landing/css/landingbaseBS.css"
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
        "propertyData": propertyData,
        "agentData": agentData,
    })
    return render(request, "landing/landingindex.html", appData)