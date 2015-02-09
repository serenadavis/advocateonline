## How to install 

Instructions for correctly setting up a virtual environment and getting started with the project are on the wiki. 

[How to Get Set Up for Linux Users](https://github.com/harvardadvocate/advocateonline/wiki/How-to-Get-Set-Up-(Linux))

[How to Get Set Up for Mac Users](https://github.com/harvardadvocate/advocateonline/wiki/How-to-Get-Set-Up-(Mac))

### Run it locally
Navigate to the root directory of the repo you just cloned ```/advocateonline``` and run

```python manage.py runserver```. Now go to ```localhost:8000``` to view the site!

## Contributing

When installing new packages, always make sure to update the requirements file.
```
pip freeze > requirements.txt
```

## Updating the database
[Dealing With Migrations](https://github.com/harvardadvocate/advocateonline/wiki/Dealing-with-Migrations)

In general, whenever you pull code, you should probably run ```python manage.py migrate``` in case someone has committed new database migrations to the repository.

You should also periodically run ```pip install -r requirements.txt``` in case someone has installed new packages. 

