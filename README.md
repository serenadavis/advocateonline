## How to install 

Instructions for correctly setting up a virtual environment and getting started with the project are on the wiki. 

[How to Get Set Up for Linux Users](https://github.com/harvardadvocate/advocateonline/wiki/How-to-Get-Set-Up-(Linux))

[How to Get Set Up for Mac Users](https://github.com/harvardadvocate/advocateonline/wiki/How-to-Get-Set-Up-(Mac))

### Run it locally
Navigate to the root directory of the repo you just cloned ```/advocateonline``` and run

```python manage.py runserver```. Now go to ```localhost:8000``` to view the site!

## Contributing

When installing new packages, always make sure to update the requirements file.
```pip freeze > requirements.txt```

## Updating the database
To update the db, run
```
python manage.py schemamigration <app_name>
```
This creates a migration in ```<appname>/migrations/```. A migration is essentially a Python script that tells South (our database migration library) how to update the database. Be sure to add this migration to the git repository so others have the migration and can update their own databases.

To actually run the migration and update your database for a specific app, run
```
python manage.py migrate <app_name>
```
To run migrations on all apps, the command is:
```
python manage.py migrate
```
In general, whenever you pull code, you should probably run ```python manage.py migrate``` in case someone has committed new database migrations to the repository.

