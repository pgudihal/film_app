
Example API Usage:
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films      -   retrieve JSON data of all films
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations  -   retrieve JSON data of all locations
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films/3 - retrieve JSON data of film with film id: 3
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films/locations/20  - retrieve JSON data of all locations for a film with film id: 20
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations/films - retrieve JSON data of all films at each location (This value is cached in a .json file not computed)
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations/films/2 - retrieve JSON data of all films at location with loc_id: 2

