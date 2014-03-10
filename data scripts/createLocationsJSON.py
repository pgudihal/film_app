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
i = 0
print len(locations)
for location in locations:
	if location:
		try:
			result = Geocoder.geocode(location+", San Francisco")
		except:
			print "ERROR of some sort, fuck it"
			pass
		time.sleep(1)
		i+=1
		print i
		if result:
			print result.coordinates
			finalLocs.append((location, result[0].coordinates[0], result[0].coordinates[1]))
with open('locations.json','w') as outfile:
	json.dump({'locations' : finalLocs}, outfile)

results = Geocoder.geocode("90 Gold Street, San Francisco")
print results[0].coordinates