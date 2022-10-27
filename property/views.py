from django.shortcuts import render
from .forms import UserInfoForm

def property(request, propertyCode=""):
    blockDisplay = "default"
    if request.user.is_authenticated:
        loggedIn = True
        userId = request.user
    else:
        loggedIn = False
        userId = ""
    userInfoForm = UserInfoForm()
    return render(request, "property/index.html",
        {"loggedIn": loggedIn,
        "userId": userId,
        "propertyBase": "property/propertyBase.html",
        "blocksTemplate": "property/blocksTemplate.html",
        "blocksDisplay": blockDisplay,
        "propCode": propertyCode,
        "propPrice" : "80,000",
        "userInfoForm": userInfoForm}
    )