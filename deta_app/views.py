from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'dhaka'

    appid = '514f80e7635420a771d1e63c485c707f'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}

    try:
        req = requests.get(url=URL, params=PARAMS)
        respos = req.json()

        if 'weather' in respos:
            description = respos['weather'][0]['description']
            icon = respos['weather'][0]['icon']
            temp = respos['main']['temp']
        else:
            description = 'N/A'
            icon = 'N/A'
            temp = 'N/A'

        date = datetime.date.today()
        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'date': date,
            'city': city,
        }

    except Exception as e:
        print(f"Error: {e}")
        context = {
            'description': 'N/A',
            'icon': 'N/A',
            'temp': 'N/A',
            'date': datetime.date.today(),
            'city': city,
        }

    return render(request, 'data_app/index.html', context)
