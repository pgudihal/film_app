from app import db

film_location = db.Table('film_location', 
	db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
	db.Column('location_id',db.Integer, db.ForeignKey('location.id'))
)

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
	locations = db.relationship('Location',secondary=film_location,
		backref=db.backref('films',lazy='dynamic'))

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
	
	def get_info(self):
		return {'id' : self.id, 'title' : self.title,\
		'production':self.production, 'actor1' : self.actor1,\
		'actor2' : self.actor2, 'actor3' : self.actor3,\
		'writer' : self.writer, 'director' : self.director,\
		'distributor' : self.distributor, 'year' : self.year,\
		'funFacts' : self.funFacts, 'locations' :  self.get_all_locations()}

	
	def get_all_locations(self):
		locAddresses = []
		for location in self.locations:
			locAddresses.append([location.id, location.address])
		return locAddresses

	def __repr__(self):
		return '<Film %r>' % self.title

class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.Text)
	lat = db.Column(db.Float)
	long = db.Column(db.Float)

	def __init__(self, address, lat, long):
		self.address = address
		self.lat = lat
		self.long = long
	
	def get_location_info(self):
		return { 'id': self.id, 'address': self.address,'lat': self.lat, 'long':self.long}
	
	def __repr__(self):
		return '<Location %r>' % self.address