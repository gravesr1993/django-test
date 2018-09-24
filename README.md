# Example Website

This is an example website created as a playground and testsite for compatability, and learning integration of components into legacy django 1.11.
Additionally testing done within django's environment is as follows

    Flushing the DB and filling with new data.
    Created and adding new pages and redirects.
    Testing integration of bootstrap elements within django.
    Creating workarounds for specific identified scenarios which had no resolution.
    Patchwork additionally as needed for touch and feel.
    Introduction of static elements to house data, to eventually push to CDN architecture instead.

# Requirements
To install all requirements, `pip install -r requirements.txt` within the src directory

    certifi==2018.8.24
    chardet==3.0.4
    click==6.7
    colorama==0.3.9
    dj-database-url==0.5.0
    Django==1.11.8
    django-crispy-forms==1.7.2
    django-extensions==2.1.2
    djangorestframework==3.8.2
    Flask==1.0.2
    gunicorn==19.9.0
    idna==2.7
    isort==4.3.4
    itsdangerous==0.24
    Jinja2==2.10
    lazy-object-proxy==1.3.1
    MarkupSafe==1.0
    mccabe==0.6.1
    Pillow==5.2.0
    plaid-python==2.3.3
    psycopg2==2.7.5
    pydotplus==2.0.2
    pyparsing==2.2.1
    pytz==2018.5
    requests==2.19.1
    six==1.11.0
    typed-ast==1.1.0
    urllib3==1.23
    Werkzeug==0.14.1
    wrapt==1.10.11

# Visualization
![alt text](https://github.com/gravesr1993/django-test/blob/master/cfehome/src/website_visualized.png "Visualized Website Backend Design")

### Tech

* [Django](https://www.djangoproject.com/) - python based backend 
* [Sublime](https://www.sublimetext.com/) - Responsive text editor
* [Bootstrap](http://getbootstrap.com/) - Boilerplate CSS for web apps
* [Django REST framework](http://www.django-rest-framework.org/) - provided REST capabilities to the project
* [Dillinger](https://dillinger.io/) - Responsive markdown editor
* [Slick](http://kenwheeler.github.io/slick/) - Workarounds for carousel tech when bootstrap was failing
* [jQuery](https://jquery.com/) - Pretty required for web development these days
* [Graphviz](https://www.graphviz.org/) - Data visualization for UML architecture
* [Django Extensions](https://django-extensions.readthedocs.io/en/latest/#) - Digraph export for conversion to UML design
* [Pydotplus](https://pydotplus.readthedocs.io/) - Intermediary for graph conversion
* [Python](https://www.python.org/) - 3.7.xx, Mandatory for backend and django


### Installation

Install the dependencies start the server.
```
Navigate to the directory cfehome

Activating the virtualENV:
    for MAC:
        ./bin/activate
    for WINDOWS:
        .\Scripts\activate
        
Navigate to cfehome\src
Run the server: "python manage.py runserver"
```

### Defaults
    superuser: superuser
    password: p@ssword
    
    user1,user2,user3
    password: p@ssword


### Todos

 - Fix spacing on carousel, caused by image loading before slick engages leaving the dynamic part static
 - Add Night Mode
 - Fully integrate and solve plaid issues
 - Clean FPS problems on parallax example

License
----
MIT
