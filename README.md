# django-sso
Simple SSO implementation in Django

## Usage

    $ python server/manage.py migrate
    $ python server/manage.py createsuperuser
    $ python server/manage.py runserver 127.0.0.1:8000

    $ python client/manage.py migrate
    $ python client/manage.py runserver 127.0.0.1:8001

When create user in <http://127.0.0.1:8000/admin>, 
it can also sign in on <http://127.0.0.1:8001/admin/login>

## License

MIT