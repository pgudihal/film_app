from app import app,db, models
import json, os
from flask import jsonify, render_template
from config import basedir

@app.route('/')
@app.route('/index.html')
def index():
	return render_template("index.html")
	
@app.route('/sfilm/api/v1/films', methods =['GET'])
def get_films():
	films = []
	for film in models.Film.query.all():
		films.append(film.get_info())
	return jsonify({'films' : films})
	
@app.route('/sfilm/api/v1/films/<int:film_id>', methods= ['GET'])
def get_film(film_id):
	return jsonify({'film':models.Film.query.filter_by(id=film_id).first().get_info()})

@app.route('/sfilm/api/v1/films/<int:film_id>/locations', methods= ['GET'])
def get_film_locations(film_id):
	return jsonify({'locations': models.Film.query.filter_by(id=film_id).first().get_all_locations()})

@app.route('/sfilm/api/v1/locations', methods= ['GET'])
def get_locations():
	locations = []
	for location in models.Location.query.all():
		locations.append(location.get_location_info())
	return jsonify({'locations' : locations})
	
@app.route('/sfilm/api/v1/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
	return jsonify({'location': models.Location.query.filter_by(id=location_id).first().get_location_info()})

#This file needs to be recreated on update of the database
#Good thing nobody can update the database muahahaha
@app.route('/sfilm/api/v1/locations/films', methods=['GET'])
def get_films_at_locations():
	#dirty hack to serve up static json since this calculation takes a while normally
	if not os.environ.get('HEROKU') is None:
		loc = json.load(open(basedir+'/filmLoc.json'))
	else:
		loc = json.load(open(basedir+'\\filmLoc.json'))
	return jsonify(loc)


@app.route('/sfilm/api/v1/locations/films/<int:location_id>', methods=['GET'])
def get_films_at_location(location_id):
	results = models.Film.query.filter(models.Film.locations.any(id=location_id)).all()
	films = []
	for film in results:
		films.append({'film_id': film.id,'title' : film.title})
	return jsonify({'films' : films})