# challenge-Corpsystem

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cd backend

python manage.py migrate

python manage.py populate

python manage.py test

python manage.py runserver

open http://127.0.0.1:8000/call-meta/99988526423/invoice/?year=2017&month=12 in browser