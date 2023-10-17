python3 -m venv .venv #creating virtual environment for the site


.\.venv\scripts\activate #to activate the virtual environment.  Console becomes:   (.venv) C:\repos\monarch-entry-only\.venv [main ≡ +2 ~0 -0 !]> 
deactivate #jump out of virtual environment

pip freeze #shows packages installed (respects virutal environment)

pip install django #install django


python manage.py runserver #to spin up the local server

python manage.py migrate  #to apply migrations for packages on to the local database

python manage.py createsuperuser #to create our first super user on the local database

python manage.py makemigrations monarchsite #this creates our migrations using the models.py in our site

python manage.py sqlmigrate monarchsite 0001 #used to see the SQL of the migration

python manage.py migrate #actually applies the migrations our database