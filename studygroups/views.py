from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

schedules = []
lengthX = 7
lengthY = 12

def index(request):
    return HttpResponseRedirect(reverse(survey))

def survey(request):
    return render(request, "survey.html")

def getSchedule(request):
    schedule = []
    for d in range(lengthX):
        timeSlots = []
        for t in range(lengthY):
            timeSlots.append(request.POST[str(t) + str(d)])
        schedule.append(timeSlots)
    schedules.append(schedule)
    printSchedules()
    return HttpResponseRedirect(reverse(survey))

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

def compareSchedules(cmpSchedules):
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
                if len(timeSlots) >= 2:
                    periods[d].append(timeSlots)
                timeSlots = []
    return periods
