TO RUN THE SERVER FROM VS CODE:
1) navigate to root file (in my case Octopus) directory
2) in cmd type "pipenv shell" <= this'll start virtual environment
3) then navigate to myproject(contains manage.py), then type "python manage.py runserver" <= this'll start srerver
4) it'll show "http://" something like this

TO MIGRATE:
1) to do migrations navigate to primary myproject directory and type in cmd "python manage.py makemigrations"
2) if want to add a row in existing data table Eg: "password = models.CharField(max_length=50, unique=True, null=True, blank=True)"
    identify null & blank then type in cmd "python manage.py makemigrations" and then "python manage.py migrate"

TO INSTALL BOOTSTRAP:
1)naviage to root file(in my case Octopus), and in cmd type:
    "pipenv install django-crispy-forms"
    "pipenv install crispy-bootstrap5"
2)then update in settings.py below INSTALLED_APPS like thsi:
    'crispy_forms',
    'crispy_bootstrap5',
3)then update in bottom of the settings.py
    CRISPY_TEMPLATE_PACK = 'bootstrap5'

TIPS IN CMD:
1) CTRL + L clear cmd
2) cd to forward directory
3) cd .. to backward directory

REQUIREMENT PAKAGES
1) pip install PyJWT
2) pip install requests