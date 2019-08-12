from django.shortcuts import render
import json
import requests
import request
# Create your views here.
def index(request):
    content={}
    return render(request, 'student/index.html', content)

def tianqi(request):
    url=f'https://www.tianqiapi.com/api/'
    params={
        'version':"v1",
        'cityid':'101101112'
    }
    resp=requests.get(url=url,params=params)

    resp = json.loads(resp.text)


    city = resp['city']
    print(city)


    day = resp['data']


    # day = resp['data'][0]['day']
    date = resp['data'][0]['date']
    humidity = resp['data'][0]['humidity']
    tem1 = resp['data'][0]['tem1']
    week = resp['data'][0]['week']
    wea = resp['data'][0]['wea']
    air_level = resp['data'][0]['air_level']
    day2 = resp['data'][0]['hours']

    # print(day)

    content={
        'day2':day2,
        'city':city,
        'day':day,
        'date':date,
        'week':week,
        'wea':wea,
        'humidity':humidity,
        'air_level':air_level,
        'tem1':tem1,

    }
    return render(request,'student/tianqi.html',content)