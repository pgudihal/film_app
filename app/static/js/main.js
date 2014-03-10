$(function(){
	//Basic Models
	var host = 'http://localhost:5000'
	var Film = Backbone.Model.extend({
		idAttribute: 'id'
	});
	var Location = Backbone.Model.extend({
		idAttribute: 'id'
	});
	var FilmsLocations = Backbone.Model.extend({
		idAttribute: 'locId'
	});
	
	//Basic Collections
	var FilmList = Backbone.Collection.extend({
		model: Film,
		url: host+'/sfilm/api/v1/films',

		parse: function(response){
			return response.films;
		}
	});
	var LocationList = Backbone.Collection.extend({
		model: Location,
		url: host+'/sfilm/api/v1/locations',
		parse: function(response){
			return response.locations;
		}
	});

	var FilmsAtLocation = Backbone.Collection.extend({
		model: FilmsLocations,
		url: host+'/sfilm/api/v1/locations/films',
		parse: function(response){
			return response.film_loc;
		}
	});

	var filmList = new FilmList();
	var locationList = new LocationList();
	var filmAtLocationList = new FilmsAtLocation();
	
	Backbone.pubSub = _.extend({}, Backbone.Events);
	
	//Set-up the map with Google Maps
	//Also fetch the locations and movies here
	var MapView = Backbone.View.extend({
		el: $('#map-canvas'),
		markers: [],
		
		initialize: function(){
			Backbone.pubSub.on('autocompleteSelected', this.getMarkersForFilm,this);
			Backbone.pubSub.on('autocompleteClosed', this.removeMarkers,this);
		
			var mapOptions = {
				center: new google.maps.LatLng(37.7833, -122.4167),
				zoom: 13
			};
			this.googleMap = new google.maps.Map(this.el, mapOptions);
			var infoWindow = new google.maps.InfoWindow();
			var self = this;
			//Fetch our list of films from the API
			filmList.fetch().done(function(){
				//Also fetch our locations to load markers
				Backbone.pubSub.trigger('filmsLoaded');
				self.fetchLocations();
			});

        },
		//Fetch Locations and place markers on the screen
		fetchLocations: function(){
			var self = this;
			locationList.fetch().done(function(){
				filmAtLocationList.fetch().done(function(){
					self.createAllMarkers();
				});

			});
		},
		createAllMarkers: function(){
			var self = this;
			locationList.each(function(loc) {
				self.createLocationMarker(loc);
			});
		},
		//Create and place markers around the map
		createLocationMarker: function(location){
			var self = this;
			var ltLn = new google.maps.LatLng(
				location.get('lat'),
				location.get('long')
			);
			marker = new google.maps.Marker({
				map: self.googleMap,
				position: ltLn,
				title: location.get('address'),
				clickable: true
			});
			self.markers.push(marker);
			var info = new google.maps.InfoWindow({content: ''});
			var filmsAtLocation;
			if(typeof filmAtLocationList.get(location.get('id'))!= 'undefined')
				filmsAtLocation = filmAtLocationList.get(location.get('id')).get('filmList')
			else
				filmsAtLocation = []

			//Place markers and put the info as the List of movies filmed there
			var windowContent = '<p><b> List of Movies filmed at ' + location.get('address') +' </b></p><p>'+filmsAtLocation.toString()+'</p>'
			bindInfo(marker, self.googleMap, info, windowContent, location.get('address'));
			function bindInfo(marker, map, info, content, address){
				google.maps.event.addListener(marker, 'mouseover', function() {
					info.setContent(content);
					info.open(map, marker);
				});
				google.maps.event.addListener(marker, 'mouseout', function() {
					info.close();
				});
			}			
		},
		removeMarkers: function(bool){
			while(this.markers.length){
				this.markers.pop().setMap(null);
			}
			if(bool)
				this.createAllMarkers()
		},
		//Get all the markers for a specific film
		getMarkersForFilm: function(film){
			var self = this;
			this.removeMarkers(false);
			var locations = film[0].get('locations');
			for(i=0; i<locations.length;i++){
				var loc = locations[i][0];
				self.createLocationMarker(locationList.get(loc));
			}
		},

	});
	
	var mapView = new MapView;
	
		//Autocomplete Search View
	var AutoCompleteInputView = Backbone.View.extend({
		el: $('#autocomplete'),
		
		initialize: function(){
			Backbone.pubSub.on('filmsLoaded',this.initializeAutoComplete);
		},
		initializeAutoComplete: function(){
			var self = this;
			$('#autocomplete').autocomplete({
				source: filmList.pluck('title'),
				minLength: 1,
				focus: function(event, ui){
					console.log('FOCUS');
					var film = filmList.where({title : ui.item.value});
					//console.log(film);
					Backbone.pubSub.trigger('autocompleteSelected',film);
				},
				select: function(event, ui){
					console.log('SELECT');
					var film = filmList.where({title : ui.item.value});
					//console.log(ui.item.value);
					Backbone.pubSub.trigger('autocompleteSelected',film);
				},
				change: function(event, ui){
					console.log('CHANGE');
					if(!ui.item){
						Backbone.pubSub.trigger('autocompleteClosed',true);
					}
				},
			});
		}
	});
	
	var autoCompleteInput = new AutoCompleteInputView();
});