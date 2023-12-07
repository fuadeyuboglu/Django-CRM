# Django CRM

## Description

A Customer Relationship Management app created using Django, Python, and MySQL.

## Overview

### Goal

To get familiar with Django framework, which I plan to use in future, before diving into details.

To see the process of web app development from developing locally and depyloyment.

With Django-CRM, user should be able to:

- Register
- Login
- Logout
- View records
- Add new records
- Delete a record
- Update a record
- Logout

### Link

- Live site url: [Django CRM](https://django-dcrm.up.railway.app/)

## Process

### Built with

- Django
- Python
- MySQL
- Bootstrap
- Railway

### What I learned

- Creating a virtual environment in Python:

  ```
  python -m venv /path/to/new/virtual/environment
  ```

- Activating existing virtual environment:

  ```
  source virt/bin/activate
  ```

- Creating a Django project:

  ```
  django-admin startproject <name of your project>
  ```

- Creating an app within a Django project:

  ```
  python manage.py startapp <name of your app>
  ```

- Adding the created app to the INSTALLED_APPS list on setting.py file:

  ```py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      <your app>,
  ]
  ```

- Configuring the database to use MySQL instead of sqlite3:

  ```py
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': '',
              'USER': '',
              'PASSWORD': '',
              'HOST': '',
              'PORT': '',
          }
      }
  ```

- Creating a database in MySQL via Python:

  ```py
    import mysql.connector

    dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'password123',

    )

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database
    cursorObject.execute("CREATE DATABASE databasename")

    print("Database has been created!")
  ```

- Migration:

  ```
    python manage.py migrate
  ```

- Creating a superuser:
  ```
    python manage.py createsuperuser
  ```

## Acknowledgments

In this Customer Relationship Management (CRM) application with Django project I havily relied on the tutorial instructed by `John Elder` that published on `freeCodeCamp.org` Youtube Channel.

I used README template provided by `frontendmentor.io`.
