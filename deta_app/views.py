import requests
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    appid = '514f80e7635420a771d1e63c485c707f'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'dhaka', 'appid':appid, 'units':'metric'}
    
    req = requests.get(url=URL, params=PARAMS)
    respos = req.json()
    description = respos['weather'][0]['description']
    icon = respos['weather'][0]['icon']
    temp = respos['main']['temp']
    date = datetime.date.today()
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'date': date,
    }
    return render(request, 'data_app/index.html',context)