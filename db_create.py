#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db, models
from flask import jsonify
import json
import os.path
db.drop_all()
db.create_all()

#create Locations
locations = json.load(open('locations.json'))

#add locations to database
for location in locations['locations']:
	loc = models.Location(location[0], location[1], location[2])
	db.session.add(loc)
db.session.commit()

#create Films
films = json.load(open('rows.json'))

lastFilm = ""
curFilm = ""
o = 0
#build film object (a bit more complicated than locations)
for i,data in enumerate(films['data']):
	if data[8] == lastFilm:		
		continue
	#Create the film object 
	#(title, production company, actor 1, actor 2, actor 3, writer, director, distributor, year, fun fact (list), locations (list)
	# Made separate variables to have explicit references
	title = ""
	prod =""
	a1 = ""
	a2 = ""
	a3 = ""
	writ = ""
	dir = ""
	dist = ""
	year = 0
	if data[8]:
		title = data[8]
	if data[12]:
		prod = data[12]
	if data[16]:
		a1 = data[16]
	if data[17]:
		a2 = data[17]
	if data[18]:
		a3 = data[18]
	if data[15]:
		writ = data[15]
	if data[14]:
		dir = data[14]
	if data[13]:
		dist = data[13]
	if data[9]:
		year = data[9]
	funfacts = ""
	if data[11]:
		funfacts += data[11]
	locList = []
	if(data[10]):
		#Query the right Location object from the db
		curLoc = models.Location.query.filter_by(address=data[10]).first()
		locList.append(curLoc)
	#loop through the rest and find the other entries with the same film
	# add the locations and funfacts from those to our film object
	for extraData in films['data'][i:]:
		if extraData[8] != title:
			continue
		if extraData[11]:
			funfacts += extraData[11]
		if extraData[10]:
			addLoc = models.Location.query.filter_by(address=extraData[10]).first()
			locList.append(addLoc)
	#add the film to the session before commit
	film = models.Film(title,prod,a1,a2,a3,writ,dir,dist,year,funfacts,locList)
	db.session.add(film)
	#Store the title of the current film so we can skip iterations in the loop
	lastFilm = title

db.session.commit()


if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
