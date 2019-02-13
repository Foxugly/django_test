rm db.sqlite3
rm __pycache__/*.pyc
rm foo/__pycache__/*.pyc
rm foo/migrations/*.py
rm foo/migrations/__pycache__/*.pyc
rm lib/__pycache__/*.pyc
rm lib/templatetags/__pycache__/*.pyc
python3 manage.py makemigrations
python3 manage.py makemigrations foo
python3 manage.py migrate
python3 manage.py createsuperuser --username test --email 'test@test.be'
python3 manage.py shell < data.py
python3 manage.py runserver