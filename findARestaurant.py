from geocode import getGeocodeLocation
import json
import httplib2
import requests

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "MV5BVBXBJVOG0UNFDDMACN1I0GRBY1VJJYNSUTECOWBNFWCX"
foursquare_client_secret = "E3FBVURIN42AEIGLL2PVRBY4YPF53PK1AYOGVIZWRNCVODZE"
version = '20151010'

url = 'https://api.foursquare.com/v2/venues/search?'

def findARestaurant(mealType,location):
    # find restaurant in given latitude/longitude
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&query=%s&ll=%s,%s&v=%s'
        % (foursquare_client_id,foursquare_client_secret,mealType,latitude,longitude,version))
    responseObject = requests.get(url)
    parsedResponse = json.loads(responseObject.text)

    # retrieve venue name and address of first restaurant in list
    foundRestaurant = parsedResponse['response']['venues'][0]
    venue_name = foundRestaurant['name']
    venue_address = foundRestaurant['location']['formattedAddress'][0]
    venue_id = foundRestaurant['id']

    # retrieve photo of restaurant
    photo_url = 'https://api.foursquare.com/v2/venues/'
    photo_payload = {
        'client_id': foursquare_client_id,
        'client_secret': foursquare_client_secret,
        'v': version,
    }
    photoResponseObject = requests.get(photo_url+venue_id+'/photos?', params=photo_payload)
    parsedPhotoResponse = json.loads(photoResponseObject.text)
    photo_url ='NO PHOTO AVAILABLE'
    if parsedPhotoResponse['response']['photos']['items']:
        photo = parsedPhotoResponse['response']['photos']['items'][0]
        photo_prefix = photo['prefix']
        photo_size = '300x300'
        photo_suffix = photo['suffix']
        photo_url = photo_prefix+photo_size+photo_suffix

    restaurant_info = {
        'name': venue_name,
        'address': venue_address,
        'photo': photo_url,
    }
    print restaurant_info['name']
    print restaurant_info['address']
    print restaurant_info['photo']
    print '\n'
    return restaurant_info
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url

if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")
