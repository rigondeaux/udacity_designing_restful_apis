import json
import requests
import httplib2

def getGeocodeLocation(inputString):
    google_api_key = 'AIzaSyDSrleoB_z868zS2Qz968lOp7xmAQ5Rm5o'
    locationString = inputString.replace(' ', '+')
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))

    # using requests
    responseContent = requests.get(url)
    parsedResponse = json.loads(responseContent.text)
    latitude = parsedResponse['results'][0]['geometry']['location']['lat']
    longitude = parsedResponse['results'][0]['geometry']['location']['lng']
    # coordinates = [latitude,longitude]
    # return coordinates
    return (latitude, longitude)

    # using httplib2
    # httpRequestObject = httplib2.Http()
    # response, content = httpRequestObject.request(url,'GET')
    # # get request. returns an array with two values -
    # # 1. the http response and 2. the content
    # parsedResult = json.loads(content)
    # print 'response header: %s \n \n'%response
    # return parsedResult
