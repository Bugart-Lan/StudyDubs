from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import *

lengthX = 7
lengthY = 12

def index(request):
    return HttpResponseRedirect(reverse(survey))

def login(request):
    """
    storage = get_messages(request)
    for message in storage:
        print(message)
    """
    return render(request, "login.html")

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        return HttpResponseRedirect(reverse(index))
    else:
        messages.add_message(request, messages.ERROR, 'Invalid credentials.')
        return HttpResponseRedirect(reverse(login))

def survey(request):
    return render(request, "survey.html")

def register(request):
    return render(request, "register.html")

def create_account(request):
    username = request.POST['username']
    student_id = request.POST['number']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        profile = Profile(user=user, student_id=student_id)
        profile.save()
        return HttpResponseRedirect(reverse(login))
    except:
        messages.add_message(request, messages.ERROR, 'Username has been taken.')
        return HttpResponseRedirect(reverse(register))



def getSchedule(request):
    schedule = ""
    for d in range(lengthX):
        for t in range(lengthY):
            schedule += '1' if request.POST[str(t) + str(d)] == 'true' else '0'
    criteria = Criteria(first_name=first, last_name=last, gpa=gpa, skills=null, schedule=schedule)
    criteria.save()
    return HttpResponseRedirect(reverse(survey))

def showCommonTime(request):
    return render(request, "common_time.html", {'ctime': commonTime(schedules)})

def printSchedules():
    for schedule in schedules:
        printSchedule(schedule)
        print()

def printSchedule(schedule):
    for d in range(lengthX):
        line = str(d) + " "
        for t in range(lengthY):
            line += str(schedule[d][t]) + " "
        print(line)

def commonTime(schedules):
    results = [[] for i in range(lengthX)]
    for d in range(lengthX):
        for t in range(lengthY):
            available = True
            for schedule in schedules:
                if not schedule[d][t]:
                    available = False
                    break
            results[d].append(int(available))
    return results

def compareSchedules(cmpSchedules, length):
    periods = [[] for i in range(lengthX)]
    for d in range(lengthX):
        timeSlots = []
        for t in range(lengthY):
            free = True
            for schedule in cmpSchedules:
                free = free and schedule[d][t]
            if free:
                timeSlots.append(t)
            if not free or t == lengthY - 1:
                if len(timeSlots) >= length:
                    periods[d].append(timeSlots)
                timeSlots = []
    return periods
