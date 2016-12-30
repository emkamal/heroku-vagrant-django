About
=====

This project might be your starting point when you want to run a Django app on Heroku
Test it at https://heroku-vagrant-django.herokuapp.com/

Setup
=====

* Fork this repository
* Start the vagrant machine and log in
```
vagrant up
vagrant ssh
cd /vagrant
```
* Login to the Heroku Toolbelt
```
heroku login
```
* Test that the app works locally
```
heroku local web
```

Test
====

* Check if the webserver is running on http://192.168.29.29:5000/

Heroku config
=============

* Create a new app
* Configure checkout from github
* Create a Heroku database
```
heroku addons:create heroku-postgresql:hobby-dev --app <<YourAppName>>
```
* Commit your changes to your github repository
* Wait for automatic deployment

PyCharm config
==============

* Create interpreter from vagrant machine
* Set python executable to
```
/home/vagrant/virtualenv/bin/python3
```
