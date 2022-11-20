from django.shortcuts import render
import urllib.request
import json


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
                            'http://api.openweathermap.org/data/2.5/weather?q=' +
                            city + '&units=metric&appid=<YOUR KEY API>').read()
        
        list = json.loads(source)

        data = {
            "city": str(list['name']),
            "country_code": str(list['sys']['country']),
            "coordinate": str(list['coord']['lon']) + ', '
            + str(list['coord']['lat']),
            "temp": str(list['main']['temp']) + ' °C',
            "pressure": str(list['main']['pressure']),
            "humidity": str(list['main']['humidity']),
            'main': str(list['weather'][0]['main']),
            'description': str(list['weather'][0]['description']),
            'icon': list['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "index.html", data)