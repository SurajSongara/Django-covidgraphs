from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .utils import overall_plot, state_data,statewise,dataf
import json
from django.core import serializers

# Create your views here.



def contactview(request):
    return render(request,'contact.html')



def statewiseview(request):
    states,labels,values=statewise()
    return render(request,'statewise.html',{"states":states,"labels":labels,"values":values})



def homeview(request):
    recent = overall_plot() 
    context = {
        'total_confirmed':recent['totalconfirmed'],
        'total_deceased':recent['totaldeceased'],
        'total_recovered':recent['totalrecovered'],
        'new_case':recent['dailyconfirmed'],
        'new_deceased':recent['dailydeceased'],
        'new_recovered':recent['dailyrecovered']
    }
    return render(request,'home.html',context=context)



def confirmedview(request):
    data=dataf("dailyconfirmed")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context={
        "ans":res,
        "head":"Confirmed Cases",
        "color":"#F25508"
        }
    return JsonResponse(context)



def deathview(request):
    data=dataf("dailydeceased")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context = {
        "ans":res,
        "head":"Death Cases",
        "color":"#BA0A03"
    }
    return JsonResponse(context)


def recoveredview(request):
    data=dataf("dailyrecovered")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context = {
        "ans":res,
        "head":"Recovered Cases",
        "color":"#2CA204"
    }
    return JsonResponse(context)


def totol_recoveredview(request):
    data=dataf("totalrecovered")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context = {
        "ans":res,
        "head":"Total Recovered",
        "color":"#2CA204"
    }
    return JsonResponse(context)


def total_deathview(request):
    data=dataf("totaldeceased")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context = {
        "ans":res,
        "head":"Total Deaths",
        "color":"#BA0A03"
    }
    return JsonResponse(context)


def total_confirmedview(request):
    data=dataf("totalconfirmed")
    res=[]
    for d in data:
        t={
            "x":d.date,
            "y":int(d.value)
        }
        res.append(t)
    context = {
        "ans":res,
        "head":"Total Confirmed",
        "color":"#F25508"
    }
    return JsonResponse(context)


def stateview(request):
    context=state_data()
    return JsonResponse(context)




