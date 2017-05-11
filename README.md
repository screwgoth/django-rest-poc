# Django REST Framework PoC

This project is a PoC for understanding and learning the Django REST Framework module.
Inside the parent project folder "puppy_store", are two Django Apps :
* puppies
* hotel

Running
-------
    cd puppy_store
    python3 manage.py runserver 0.0.0.0:8000

puppies
-------
This app is direct implementation of a tutorial explaining use of the [Django REST Framework](http://www.django-rest-framework.org/) from the excellent blog titled :
[Test Driven Development of a Django RESTful API](https://realpython.com/blog/python/test-driven-development-of-a-django-restful-api/)


hotel
-----
This app is a PoC of implementation of an REST API which has the following features:
- It does NOT use Django Models. Instead it calls a third-party public API and returns it's Response
- The GET API also contains parameters
