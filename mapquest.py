import requests
import json

consumer_key = 'Sxtc7BNdLj5VA3dpg3oLwzqbRTQzy4Mj'
consumer_secret = ' VYKOvBsWcO1dEcz7'

location = "Washington,DC"
response = requests.get("http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}".format(consumer_key, location))
object = response.json()
print(object["results"][0]["locations"][0]["latLng"]["lat"])

#print(response.text)
