from django.shortcuts import render, redirect

def getLogin(request):
	return render(request, "login.html")

def getRegister(request):
  return render(request, "register.html")

def loginUser(request):
  if request.method == "POST":
    credentials = request.POST["credentials"]
    password = request.POST["password"]

def registerUser(request):
  if request.method == "POST":
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    return redirect("/success")

def success(request):
  return render(request, "success.html");