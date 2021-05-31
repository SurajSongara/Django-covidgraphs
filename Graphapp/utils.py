import requests
import json

def overall_plot():
    data=requests.get('https://api.covid19india.org/data.json')
    res=json.loads(data.content)
    recent=res['cases_time_series'][-1]
    return recent



class State:
    def __init__(self,name,active,confirmed,recovered,deaths,todayconfirmed,todaydeath,todayrecovered) -> None:
        self.name=name
        self.active=active
        self.confirmed=confirmed
        self.recovered=recovered
        self.deaths=deaths
        self.todayrconfirmed=todayconfirmed
        self.todaydeath=todaydeath
        self.todayrecovered=todayrecovered 


def statewise():
    data=requests.get('https://api.covid19india.org/data.json')
    res=json.loads(data.content)
    states=[]
    labels=[]
    values=[]
    for state in res['statewise']:
        name=state['state']
        active=state['active']
        confirmed=state['confirmed']
        recovered=state['recovered']
        deaths=state['deaths']
        todayconfirmed=state['deltaconfirmed']
        todaydeath=state['deltadeaths']
        todayrecovered=state['deltarecovered']
        if name=="Total":
            Total=State(name,active,confirmed,recovered,deaths,todayconfirmed,todaydeath,todayrecovered)
        elif name=="State Unassigned":
            pass
        else:
            labels.append(name)
            values.append(active)
            states.append(State(name,active,confirmed,recovered,deaths,todayconfirmed,todaydeath,todayrecovered))
    states.append(Total)
    return states,labels,values


def state_data():
    data=requests.get('https://api.covid19india.org/data.json')
    res=json.loads(data.content)
    states={}
    for state in res['statewise']:
        name=state['state']
        active=state['active']
        confirmed=state['confirmed']
        recovered=state['recovered']
        deaths=state['deaths']
        x=[active,confirmed,recovered,deaths]
        states[name]={
            "series":[int(i) for i in x]
        }
    return states



class Data:
    def __init__(self,date,value):
        self.date=date
        self.value=value


def dataf(type="dailyconfirmed"):
    data=requests.get('https://api.covid19india.org/data.json')
    res=json.loads(data.content)
    result=[]
    for case in res['cases_time_series']:
        d=case['date']
        v=case[type]
        result.append(Data(d,v))
    return result

