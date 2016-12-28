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

url = 'https://api.foursquare.com/v2/venues/search?'

def findARestaurant(mealType,location):
    geocode = getGeocodeLocation("Sydney, Australia")
    payload = {
                'client_id': foursquare_client_id,
                'client_secret': foursquare_client_secret,
#                'll': '40.7,-74',
                'v': '20151010',
                'near': 'Sydney',
                'query': 'sushi'
                }
    responseObject = requests.get(url, params=payload)
    parsedResponse = json.loads(responseObject.text)
    print responseObject.url
    return parsedResponse
    # latitude = parsedResponse['results'][0]['geometry']['location']['lat']
    # longitude = parsedResponse['results'][0]['geometry']['location']['lng']
    # return (latitude, longitude)

	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url


# if __name__ == '__main__':
#     findARestaurant("Pizza", "Tokyo, Japan")
#     findARestaurant("Tacos", "Jakarta, Indonesia")
#     findARestaurant("Tapas", "Maputo, Mozambique")
#     findARestaurant("Falafel", "Cairo, Egypt")
#     findARestaurant("Spaghetti", "New Delhi, India")
#     findARestaurant("Cappuccino", "Geneva, Switzerland")
#     findARestaurant("Sushi", "Los Angeles, California")
#     findARestaurant("Steak", "La Paz, Bolivia")
#     findARestaurant("Gyros", "Sydney Australia")

print(findARestaurant("sushi","Sydney"))
