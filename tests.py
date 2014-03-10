#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import Film, Location

##These are *very* basic unit tests
##To run these tests you need to create a test.db from the db_create script
## ./db_create.py and make sure the config is set to test.db not app.db
##Otherwise none of them will run

## TODO: More thorough unit tests
# TODO: Test json output from jsonify

class TestCase(unittest.TestCase):
	def setup(self):
		app.config['TESTING'] = True
		app.config['CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'test.db')
		self.app = app.test_client()

		
	def tearDown(self):
		db.session.remove()
		
	def test_Film(self):
		##Test to see if there are 247 entries of films in the db
		f = Film.query.all()
		assert len(f) == 247
		##Test get_info SETUP
		f = Film.query.filter_by(id=1).first().get_info()
		assert f['title'] == "180"
		assert f['funFacts'] == ''
		assert f['production'] == 'SPI Cinemas'
		assert f['distributor'] == ''
		assert f['director'] == 'Jayendra'
		assert f['writer'] == 'Umarji Anuradha, Jayendra, Aarthi Sriram, & Suba '
		assert f['year'] == 2011
		assert f['actor1'] == 'Siddarth'
		assert f['actor3'] == 'Priya Anand'
		assert f['actor2'] == 'Nithya Menon'
		##Test get_all_locations MODELS/VIEWS
		f = Film.query.filter_by(id=1).first().get_all_locations()
		assert len(f) == 8
		##Test a film with no location MODELS
		f = Film.query.filter_by(title='48 Hours').first().get_info()
		assert f['locations'] == []
		
	def test_Location(self):
		##Test to see if there are 561 entries of Locations in the db SETUP
		l = Location.query.all()
		assert len(l) == 561
		##Test get_location_info MODELS
		l = Location.query.filter_by(id=1).first().get_location_info()
		assert l['lat'] == 37.7889293 and l['long'] == -122.3930447\
			and l['id'] == 1 and l['address'] == '5th and Beale Streets'
		##Test get films at location VIEWS
		l = Film.query.filter(Film.locations.any(address='Golden Gate Bridge')).all()
		assert len(l) == 26
if __name__ == '__main__':
	unittest.main()