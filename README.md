
Project Selection
==================
SF Movies - Create a service that shows on a map where movies have been filmed in San Francisco. The user should be able to filter the view using autocompletion search.

Track + Experience + Reasoning
========================
**Full-stack**
###Backend - Python/Flask - db in Postgresql(heroku) and sqlite (local)
**Experience with Flask**
It's been a couple years since I've done proper web development, but back then my primary experience was in Ruby on Rails. I've fiddled here and there with Sinatra as well. When I spoke with Andre who mentioned that the bulk of the work at Uber is in Python I decided I'd try to do the coding challenge in Python. 

I have some experience in Python but not in web development in Python so I was pretty much coming into Flask fresh. Flask was very light and surprisingly easy to pick up. I hit up a couple tutorials online to get through a few snags that I hit.

1. Structuring a Flask application was a bit tricky at first- I used a few scripts from Miguel Grinberg's excellent tutorial series on Flask to help me get started
2. Deployment to Heroku had me a bit stumped because of migrating from sqlite to postgresql but I eventually figured that out as well

*Some notes regarding Backend implementation:*

I downloaded the data from SF Data instead of accessing it directly from the online API. I took the JSON file from the SFData website and loaded it into a sqlite (postgresql on Heroku) database along with some changes to the data (geocoded lat/lng coordinates etc). Then I used Flask to create a Read-only API for the information that I have. 

I chose not to implement all of CRUD primarily due to the fact that it really isn't necessary for my front-end and I didn't want to have public C,U,D functions available (I thinks those would be better under user authentication which I didn't implement). Implementing authentication would be on the list of future enhancements.

Example API Usage:
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films      -   retrieve JSON data of all films
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations  -   retrieve JSON data of all locations
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films/3 - retrieve JSON data of film with film id: 3
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/films/locations/20  - retrieve JSON data of all locations for a film with film id: 20
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations/films - retrieve JSON data of all films at each location (This value is cached in a .json file not computed)
* GET http://filmsinsf.herokuapp.com/sfilm/api/v1/locations/films/2 - retrieve JSON data of all films at location with loc_id: 2

These are a few working examples. Flask allows me to create new routes to serve API requests pretty easily which was a nice surprise. My testing for this backend is pretty limited. I wrote a few unit-tests but they don't really cover the range of operations. That's definitely something I'd work on given more time on this.

###Frontend - Backbone.js
I have pretty much no real experience with front-end technologies like Backbone, Angular, or Knockout etc. When I used rails I mostly stayed to backend work and didn't venture much into frontend territory. Working with Backbone.js was totally new territory for me. I figured I'd give it a shot. 

Despite the lack of experience I found myself acclimating to the structure of Backbone. I have experience in Javascript from using the Unity Engine (albeit a modified form of javascript) and experience in MVC frameworks like Rails so I was able to grasp the basic concepts quickly. I do wish I had learned about the '.pluck()' method earlier though. Would have saved me about a half hour of refactoring code. I didn't test the front-end much from a unit-testing perspective, mostly because I was focused on actually having a front-end.

To be honest this was the most challenging part of the assignment for me and where I spent a bulk of my time on this project - between researching and iterating on code-. (Backbone has the most amazing annotated source code I have ever seen.) My lack of experience with Backbone shows through the fact that not much data is available on the front-end compared to the data available on the back-end (stuff like actors, writers, fun facts etc). Despite all that I'm glad I went with Backbone, learning this definitely helps me understand more about the way modern websites are constructed on the front-end. 

Trade-offs
==========
If I had more time I compiled a list of things I would probably work on
1. User Authentication to allow full range of CRUD on the API

2. Fix the autocomplete issue on the search where it doesn't always repopulate the markers

3. More time on Front-end to display more data about each film when selected

4. Link the film to its imdb page to allow the user to get more info

5. Security enhancements to the whole app in general

6. General UI enhancements and UX enhancements

7. Use/learn Require.js to split the .js files into more readable chunks


Resume
==========
http://bit.ly/1h5S2fi

