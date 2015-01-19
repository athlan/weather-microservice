Weather Microservice
====================

This is simple microservice that provides information about weather.

Author: Piotr Pelczar

Weather microservice starts web server and provide weather conditions data as JSON API for selected location using Wunderground API. Results are cached into Redis key-value database.

Futhermore there is a guard level that 

Data is fetched from abstraction layer called Repository, and there are 3 implementations of Weather Respository:
* `Wunderground` - base repository fetching data directly from Wunderground API.
* `WundergroundApiLimitGuard` - repository proxy prevents calling API more times than is allowed by limits.
* `Cached` - each request is cached locally.

The app is based on Flask REST frmework utilizing Dependency Injection known from Spring (Spring Python), named instances of classes are declared in `app-context.yml`.

Used libraries:
* Flask
* Flask REST
* spring-python for Dependency Injection
* PyYAML
* Redis

# API

# Setup

## Requirements:

* Python 2.7
* virtualenv

## Installation:

* Create virtualenv
```
$ virtualenv env
$ source env/bin/activate
```
* Install dependencies
```
pip install -r requirements.txt
```
* You are ready!

To deactivate virtualenv just type:
```
$ deactivate
```

## Run app:

```
python app.py
```
or
```
python app.py [-h <host=0.0.0.0>] [-p <port=5000>] [-e <env=prod|dev>]
```

Make request:
```
curl http://localhost:5000/api/v1.0/weather/conditions/CA/San_Francisco
```

## Configuration

* config/parameters.yml (copy from config/parameters.yml.dist first)
* config/app-context.yml (set cache TTL)

## References

* http://docs.spring.io/spring-python/1.2.x/sphinx/html/objects-yamlconfig.html
* http://www.rafekettler.com/magicmethods.html
