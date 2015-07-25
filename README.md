pybigdata
=================

MongoDB
-----------------
We use MongoDB for storage of our data. Download and install mongo from here: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/
Start the mongo daemon with the following command: `mongod`

Creating a virtual environment
-----------------
We keep all our python related dependencies seperate from any that might be on the system. Thus we recommend installing virtualenv for python: 
- `pip install virtualenv`
- `cd my_project_folder`
- Creating a virtual environment: `virtualenv virtual_env_name`
- Within your project folder, type: `source venv/bin/activate`, to activate the virtual environment. 

Now any python packages installed will be only visible in this isolated environment.
**Note:** always remember to activate the virtual environment before running the application, otherwise references to your dependencies will not be picked up outside the environment causing errors.

PyMongo
-----------------
This application uses PyMongo, the python driver to connect to Mongo. After the mongo instance has been installed and setup, you can import your JSON/CSV data using this command: 
`mongoimport --db <database-name> --collection <collection-name> --drop --file <path/to/dataset.json>`
For more details: https://docs.mongodb.org/getting-started/python/introduction/

Flask
-----------------
Flask is a python microframework, akin to what Sinatra is to Ruby. We use Flask as our HTTP server or resource provider. Flask can be installed using pip: `pip install flask`
For details and documentation: http://flask.pocoo.org/

Qwestjs
----------------
Qwest.js is a lightweight AJAX library we use to make HTTP calls to the flask server to get our data. Qwest can be installed using any of the following commands:

- `jam install qwest`
- `bower install qwest`
- `npm install qwest --save-dev`

**Note:** We recommend installing bower to manage your javascript packages: http://bower.io/

Leaflet
---------------
Leaflet is an open source javascript library for interactive maps, that employs open street map data. You can include the library in your HTML page or download it here: http://leafletjs.com/examples/quick-start.html.


