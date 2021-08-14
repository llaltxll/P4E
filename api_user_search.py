import os

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# the google api key is stored on the dev machine in an eviroment variable
api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
# print(api_key)

# if have no api key
if api_key == None:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	parms = dict()
	parms['address'] = address
	if api_key != False: parms['key'] = api_key
	url = serviceurl + urllib.parse.urlencode(parms)

	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read().decode()
	print('Retrived', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] !='OK':
		print('==== Failure To Retrive ====')
		print(data)
		continue
	print(json.dumps(js, indent=4))

	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print('lat', lat, 'lng', lng)
	location = js['results'][0]['formatted_address']
	country_code = js['results'][0]['address_components'][3]['short_name']
	print(location," ,",country_code)