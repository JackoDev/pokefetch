# Pokefetch - a use for the PokeApi


## Description

A Pokemon is a mystical creature that belongs to a fictional world, designed
and managed by the Japanese companies Nintendo, Game Freak and
Creatures. The Pokemon world is available on manga, anime adaptions, games,
retail stores and many more places.
The depth of this virtual world allows to have mountains of data only to describe
completely a Pokemon and its relations around the universe. This information is
available on the PokeApi (https://pokeapi.co/docs/v2.html).

The project contains the follow components:

* A Command that receives as its only parameter an ID, representing
the Evolution Chain to fetch and store the following information:
    • Name
    • Base stats (for the 6 categories)
    • Height
    • Weight
    • Id
    • Evolutions

The command works with the `main.py` file:

  * `/pokefetch/main.py`
  
  To start this script, execute:

```
$ python3 main.py
```

This command extract the info of the pokeapi and store the data fetched
into the MongoDB for the later acces of the web service.


*  A Web Service which only parameter is the “name” of a Pokemon
search. This service must not do a request towards the PokeApi. The
response must include the following information:
    • Pokemon details available
    • Include for all the evolutions related
        • Evolution type (Preevolution / Evolution)
        • Id
        • Name

The web service starts with the `api.py` file:

  * `/pokefetch/webServ/api.py`
  
  To start this script and run the web server, execute:

```
$ python3 api.py
``` 

This script will initialize a web server in your `localhost`:

```
MongoDB version is 4.2.8
* Serving Flask app "api" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 
```

After this you would open your web browser and go to `http://127.0.0.1:5000/<name>`

Replace '<name>' with the Pokemon's name to search the data about it.

The project uses the Atlas cloud service for the mongoDB system data bases.


## Environment

* __OS:__ Ubuntu 18 LTS / Windows 10 (with WSL for Win10)
* __language:__ Python 3
* __application server:__ Flask 1.1.2, Jinja2 2.11.2
* __database:__ mongoDB Atlas DB
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)


## Authors

* Javier Cañón, [jackodev](https://github.com/JackoDev)

## License

MIT License

*BUGS
Detected so far:
  - Working on it:
    + Duplicate docs in mongoDB produce no data available in the web service consulting
    + Optimization in main algorythm changing the if for a loop
