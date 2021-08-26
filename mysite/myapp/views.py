from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import forms
from . import models
import pandas as pd
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def index(request):
    context = {

    }#context
    return render(request, "main.html", context = context)
# Create your views here.

def usState(request):
    url = 'https://raw.githubusercontent.com/jeffcore/covid-19-usa-by-state/master/COVID-19-Cases-USA-By-State.csv'
    df = pd.read_csv(url)
    df = df.iloc[:, ::-1]
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]
    if request.method == "POST": 
        dateFormIns = forms.dateForm(request.POST)
        stateFormIns = forms.stateForm(request.POST)       
        if dateFormIns.is_valid() and stateFormIns.is_valid():
            dateFilture = dateFormIns.cleaned_data["date"],
            stateFilture = stateFormIns.cleaned_data["state"]
            date =  dateFilture[0]
            state = stateFilture
            if state != '' and date !='':
                stateBool = df['State'] == state
                df = df[stateBool]
                df = df.filter(items=['State', date])
            elif  state != '' and date == '': 
                 stateBool = df['State'] == state
                 df = df[stateBool]
            elif  state == '' and  date != '': 
                df = df = df.filter(items=['State', date])
        dateFormIns = forms.dateForm()
        stateFormIns = forms.stateForm()
    else:
        dateFormIns = forms.dateForm()
        stateFormIns = forms.stateForm()        
    context = {
        "dateform" : dateFormIns,
        "stateform" : stateFormIns,
        "df":df, 
    }
    return render(request, "usState.html",context = context)
# Create your views here.

def keycountryies(request):
    url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/key-countries-pivoted.csv'
    df = pd.read_csv(url)
    df = df.iloc[:, ::-1]
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]
    if request.method == "POST": 
        dateFormIns = forms.fullDateForm(request.POST)
        stateFormIns = forms.stateForm(request.POST)       
        if dateFormIns.is_valid() and stateFormIns.is_valid():
            dateFilture = dateFormIns.cleaned_data["date"],
            stateFilture = stateFormIns.cleaned_data["state"]
            date =  dateFilture[0]
            state = stateFilture
            if state != '' and date !='':
                dateBool = df['Date'] == date
                df = df[dateBool]
                df = df.filter(items=['Date', state])
            elif  state == '' and date != '': 
                 dateBool = df['Date'] == date
                 df = df[dateBool]
            elif  state != '' and  date == '': 
                df = df = df.filter(items=['Date', state])
        dateFormIns = forms.fullDateForm()
        stateFormIns = forms.stateForm()
    else:
        dateFormIns = forms.fullDateForm()
        stateFormIns = forms.stateForm()        
    context = {
        "dateform" : dateFormIns,
        "stateform" : stateFormIns,
        "df":df, 
    }
    return render(request, "row.html",context = context)


def usaDeath(request):
    url = 'https://raw.githubusercontent.com/jeffcore/covid-19-usa-by-state/master/COVID-19-Cases-USA-By-State.csv'
    df = pd.read_csv(url)
    df = df.iloc[:, ::-1]
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]
    if request.method == "POST": 
        dateFormIns = forms.dateForm(request.POST)
        stateFormIns = forms.stateForm(request.POST)       
        if dateFormIns.is_valid() and stateFormIns.is_valid():
            dateFilture = dateFormIns.cleaned_data["date"],
            stateFilture = stateFormIns.cleaned_data["state"]
            date =  dateFilture[0]
            state = stateFilture
            if state != '' and date !='':
                stateBool = df['State'] == state
                df = df[stateBool]
                df = df.filter(items=['State', date])
            elif  state != '' and date == '': 
                 stateBool = df['State'] == state
                 df = df[stateBool]
            elif  state == '' and  date != '': 
                df = df = df.filter(items=['State', date])
        dateFormIns = forms.dateForm()
        stateFormIns = forms.stateForm()
    else:
        dateFormIns = forms.dateForm()
        stateFormIns = forms.stateForm()        
    context = {
        "dateform" : dateFormIns,
        "stateform" : stateFormIns,
        "df":df, 
    }
    return render(request, "usaDeath.html",context = context)


def register(request):
    if request.method == "POST":
        regFormIns = forms.RegistrationForm(request.POST)
        if regFormIns.is_valid():
            regFormIns.save()
            return redirect("/login/")
    else:
        regFormIns = forms.RegistrationForm()
    context = {
        "form":regFormIns,
    }
    return render(request, "registration/register.html", context=context)

def logoutUserOut(request): 
    logout(request)
    return redirect("/login/")


@login_required
def chatrooms(request, room_name):
    return render(request, 'chat.html', {
        'room_name':room_name
        })
