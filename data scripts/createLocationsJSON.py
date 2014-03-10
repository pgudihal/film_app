import json, time
from pygeocoder import Geocoder
#load the json file from SFData
rows = json.load(open('rows.json'))

#Variable to store the address
address = []

#Get the address
for data in rows['data']:
	address.append(data[10])
	
#remove dupes
locations = list(set(address))
finalLocs = []
print len(locations)
#Build location data and Geocode lat/lng coordinates for easy use later on
for location in locations:
	if location:
		try:
			result = Geocoder.geocode(location+", San Francisco")
		except:
			print "ERROR of some sort,move on"
			pass
		# To avoid Query overload
		time.sleep(1)
		if result:
			finalLocs.append((location, result[0].coordinates[0], result[0].coordinates[1]))
			
#Write to a json file
with open('locations.json','w') as outfile:
	json.dump({'locations' : finalLocs}, outfile)
