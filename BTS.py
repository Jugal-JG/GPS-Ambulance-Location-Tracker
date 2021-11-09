from googleplaces import GooglePlaces, types, lang
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import json

API_KEY='AIzaSyCmM3vv3uPBSzAZFdjPXwvi6pnc8HKYCA4'

geolocator= Nominatim(user_agent="hack")
address=input()
location=geolocator.geocode(address)
google_places=GooglePlaces(API_KEY)
query_result=google_places.nearby_search(
    lat_lng={'lat':float(location.latitude),'lng':float(location.longitude)},
    radius=5000,
    types=[types.TYPE_HOSPITAL])

if query_result.has_attributions:
    print(query_result.html_attributions)
for place in query_result.places:
    print(place.name)
    print("Latitude", place.geo_location['lat'])
    print("Longitude", place.geo_location['lng'])
    print().
