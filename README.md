# asyncio

testing out asyncio

Trying out calling several sync functions from a sync env through asyncio.
It gets us a 10x speed up without changing from uwsgi to asgi.

```
$ pipenv install
$ pipenv run FLASK_APP=app.py flask run
$ pipenv run python test.py
```
