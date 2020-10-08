# For windows setup
## Download python:3.8.3
    https://www.python.org/downloads/release/python-383/

## Install virtualenv
    pip install virtualenv 

## create virtual environments
    virtualenv " your virtual env name"

## activate virtualenv
    "your env name"\Scripts\activate

## clone repogitory
    1. git clone https://github.com/palprem/assignment-credicxo.git
    2. cd assignment-credicxo/backend
    3. pip install -r requirements.txt
    4. python manage.py makemigrations
    5. python manage.py migrate
    6. python manage.py runserver