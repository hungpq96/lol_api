# lol_api

### Config database

database design: https://dbdesigner.page.link/3EcintFx3oycCPef6
```
cp config.cnf.example config.cnf
```

### Run project

```
// start venv
pipenv shell

// create database
mysql -u root -p
create database lol;
exit

// create & run migrations
cd lol
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

// start server
pipenv run python manage.py runserver
```
