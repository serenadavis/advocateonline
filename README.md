## How to install 

### Clone the repo
```git clone git@github.com:harvardadvocate/advocateonline.git```

### Set up a virtual environment
If you need help setting up a virtual environment, please read through [this guide](http://www.jeffknupp.com/blog/2013/12/18/starting-a-django-16-project-the-right-way) to setting up a Django 1.6 project the right way. If you're using virtualenvwrapper (highly recommended), you can simply enter
```mkvirtualenv advocateonline``` to get going.

### Install the requirements
```pip install -r requirements.txt```

If you get an error like ```EnvironmentError: mysql_config not found``` then it means that you need to install libmysqlclient-dev like so:

```sudo apt-get install libmysqlclient-dev```

If you get an error while installing it, make sure you update your sources and then run ```apt-cache policy libmysqlclient-dev```.

### Run it locally
Navigate to the root directory of the repo you just cloned ```/advocateonline``` and run
```python manage.py runserver```. Now go to ```localhost:8000``` to view the site!

## Contributing

When installing new packages, always make sure to update the requirements file.

```pip freeze > requirements.txt```