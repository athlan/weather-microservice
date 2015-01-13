Weather Microservice
====================

This is simple microservice that provides information about weather.

Author: Piotr Pelczar

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

## References

* http://docs.spring.io/spring-python/1.2.x/sphinx/html/objects-yamlconfig.html
* http://www.rafekettler.com/magicmethods.html
