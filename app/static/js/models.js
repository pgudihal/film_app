$(function(){
	//Basic Models
	var Film = Backbone.Model.extend();
	var Location = Backbone.Model.extend();

	//Basic Collections
	var FilmList = Backbone.Collection.extend({
		model: Film,
		url: 'http://localhost:5000/sfilm/api/v1/films',

		parse: function(response){
			return response.films;
		}
	});
	var LocationList = Backbone.Collection.extend({
		model: Location,
		url: 'http://localhost:5000/sfilm/api/v1/locations',
		parse: function(response){
			return response.locations;
		}
	});



	var filmList = new FilmList()
	var locationList = new LocationList()
	locationList.fetch({
		success: function(collection){
			console.log(collection);
		}
	});
	
	filmList.fetch({
		success: function(collection){
			console.log(collection);
		}
	});
});
