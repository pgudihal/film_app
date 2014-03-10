from app import db
#Association table for many-to-many relationship between Films and Locations
film_location = db.Table('film_location', 
	db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
	db.Column('location_id',db.Integer, db.ForeignKey('location.id'))
)
#Film Model
class Film(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	production = db.Column(db.String(100))
	actor1 = db.Column(db.String(100))
	actor2 = db.Column(db.String(100))
	actor3 = db.Column(db.String(100))
	writer = db.Column(db.Text)
	director = db.Column(db.String(100))
	distributor = db.Column(db.String(100))
	year = db.Column(db.Integer)
	funFacts = db.Column(db.Text)
	#Backref for locations so that we can access them
	locations = db.relationship('Location',secondary=film_location,
		backref=db.backref('films',lazy='dynamic'))
	
	#Basic init
	def __init__(self, title, p,a1,a2,a3,w,dir,dist,yr,ff, locations):
		self.title = title
		self.production = p
		self.actor1 = a1
		self.actor2 = a2
		self.actor3 = a3
		self.writer = w
		self.director = dir
		self.distributor = dist
		self.year = yr
		self.funFacts = ff
		self.locations = locations
	
	#Pseudo-serialization since jsonify doesn't let me do as much as I'd like
	def get_info(self):
		return {'id' : self.id, 'title' : self.title,\
		'production':self.production, 'actor1' : self.actor1,\
		'actor2' : self.actor2, 'actor3' : self.actor3,\
		'writer' : self.writer, 'director' : self.director,\
		'distributor' : self.distributor, 'year' : self.year,\
		'funFacts' : self.funFacts, 'locations' :  self.get_all_locations()}

	#Clean up the get_info a bit
	def get_all_locations(self):
		locAddresses = []
		for location in self.locations:
			locAddresses.append([location.id, location.address])
		return locAddresses
	#basic __repr__ 
	def __repr__(self): #pragma: no cover
		return '<Film %r>' % self.title
#Location Model
class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.Text)
	lat = db.Column(db.Float)
	long = db.Column(db.Float)
	
	#Lat/Long are computed in the createLocationsJSON file which creates
	# a json file to just read the geocoded data so that we can fill this 
	# table in
	def __init__(self, address, lat, long):
		self.address = address
		self.lat = lat
		self.long = long
	#Like above this is a pseudo-serialization for jsonify
	def get_location_info(self):
		return { 'id': self.id, 'address': self.address,'lat': self.lat, 'long':self.long}
	
	def __repr__(self): #pragma: no cover
		return '<Location %r>' % self.address