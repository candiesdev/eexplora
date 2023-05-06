from ast import Pass
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.db.models import Case, When, Value, IntegerField, Q
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
from .models import MenuItem

from .forms import SessionLogin, SessionAuthenticate

# Menu constructor and orderer function

def menuConstructor(itemsList):
    name="name"
    q = Q()
    for itemValue in itemsList:
        q |= Q(**{name: itemValue})
    ordering = Case(
        When(q & Q(name='return'), then=Value(0)),
        When(q & Q(name='login'), then=Value(1)),
        When(q & Q(name='home'), then=Value(2)),
        default=Value(3),
        output_field=IntegerField(),
        )
    menuItems = MenuItem.objects.filter(q).order_by(ordering)
    return menuItems

# Main function to handle session view

def sessionView(request):

# Default variables value setting

    action = alert = ""
    prev = "/usr"
    userId = ""
    userEmail = ""
    sessionTemplate = ""
    loginData = {}
    activeApp = "login"
    colorPalette = "none"
    activeApp = True
    appStyle = "/usr/css/usrbase.css"
    loginData.update({
        "activeApp": activeApp,
        "appStyle": appStyle,
    })

    if request.method == "POST":
        if "action" in request.POST:
            action = request.POST["action"]
        if "prev" in request.POST:
            prev = request.POST["prev"]
    elif "action" in request.GET:
        action = request.GET["action"]
    if "prev" in request.GET:
        prev = request.GET["prev"]
    if "palette" in request.GET:
        colorPalette = "palette" + request.GET["palette"]        

    if request.user.is_authenticated:
        logged = True
        alert = "Autenticado"
    else:
        alert = "No autenticado"
        logged = False

# Return to previous or default url in case of athentication request for authenticated session

    if logged and (action == "login" or action == "password" or action == "authenticate"):
        return redirect(prev)

# Handle login request

    elif action == "login":
        logged = False
        alert = "No autenticado"
        action = "enterPass"
        sessionTemplate = "userLogin"
        sessionForm = SessionLogin()
        loginData.update({
        "action": action,
        "prev": prev,
        "alert": alert,
        "sessionTemplate" : sessionTemplate,
        "sessionForm" : sessionForm,
        "activeApp": activeApp,
        "colorPalette": colorPalette})
        return render(request, "usr/sessionindex.html", loginData)
    
# Handle password request

    elif action == "enterPass":
            userId = request.POST["userId"]
            logged = False
            alert = "No autenticado"
            if User.objects.filter(username=request.POST["userId"]).exists():
                action = "authenticate"
                sessionTemplate = "userPass"
                sessionForm = SessionAuthenticate(userId)
                loginData.update({
                "action": action,
                "prev": prev,
                "alert": alert,
                "sessionTemplate" : sessionTemplate,
                "sessionForm" : sessionForm,
                "activeApp": activeApp,
                "colorPalette": colorPalette})
                return render(request, "usr/sessionindex.html", loginData)
            else:
                alert = "user_error"
                action = "login"
                sessionTemplate = "userError"
                loginData.update({
                "action": action,
                "prev": prev,
                "alert": alert,
                "sessionTemplate" : sessionTemplate,
                "userId": userId,
                "activeApp": activeApp,
                "colorPalette": colorPalette})
                return render(request, "usr/sessionindex.html", loginData)
            
# Authenticate user

    elif action == "authenticate":
        if request.method == 'POST':
            username = request.POST['userId']
            password = request.POST['userPass']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                loggedIn = True
                return redirect(prev)
            else:
                alert = "password_error"
                action = "login"
                sessionTemplate = "passwordError"
                loginData.update({
                "action": action,
                "prev": prev,
                "alert": alert,
                "sessionTemplate" : sessionTemplate,
                "userId": userId,
                "activeApp": activeApp,
                "colorPalette": colorPalette})
                return render(request, "usr/sessionindex.html", loginData)

# Logout session

    elif action == "logout":
        try:
            logout(request)
            alert = "No autenticado"
            logged = False
            return redirect(prev)
        except:
            alert = "Desconexión fallida"
            return redirect(prev)

# User info for authenticated session

    elif logged:
        itemsList = ["logout", "home"]
        if prev!="/usr":
            itemsList.append("return")
        menuItems = menuConstructor(itemsList)

        sessionMenu = {}
        for menu in menuItems:
            title = menu.title
            titleUrl = menu.url
            if title == "return":
                titleUrl = prev
            sessionMenu.update({ title : titleUrl })

        logged = True
        alert = "Autenticado"
        sessionTemplate = "userInfo"
        userId = request.user.username
        userEmail = request.user.email
        loginData.update({
        "action": action,
        "prev": prev,
        "alert": alert,
        "sessionTemplate" : sessionTemplate,
        "userId": userId,
        "userEmail": userEmail,
        "sessionMenu" : sessionMenu,
        "activeApp": activeApp,
        "colorPalette": colorPalette})
        return render(request, "usr/sessionindex.html", loginData)

# If no other option applicable go to user authentication index

    else:
        itemsList = ["login", "home"]
        if prev!="/usr":
            itemsList.append("return")
        menuItems = menuConstructor(itemsList)

        sessionMenu = {}
        for menu in menuItems:
            name = menu.name
            title = menu.title
            titleUrl = menu.url
            if name == "return":
                titleUrl = prev
            sessionMenu.update({ title : titleUrl })

        sessionTemplate = "sessionIndex"
        loginData.update({
        "sessionTemplate" : sessionTemplate,
        "sessionMenu" : sessionMenu,
        "activeApp": activeApp,
        "colorPalette": colorPalette})
        return render(request, "usr/sessionindex.html", loginData)