from django.shortcuts import render
import requests
# Create your views here.
def geo_location(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR'," ") or request.META.get('REMOTE_ADDR')
    url = 'http://api.ipstack.com/'+str(ip)+'?access_key=ab79ae78507a9adb4388bff9226a4bce'
    #url = 'http://api.ipstack.com/157.44.158.198?access_key=ab79ae78507a9adb4388bff9226a4bce'
    response = requests.get(url)
    data = response.json()
    return render(request, 'my_location/address.html',data)


    
