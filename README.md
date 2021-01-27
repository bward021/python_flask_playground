## Database Setup
- If you need to setup your database you will need to do the following inside a python repl while in your pipenv shell.
  - If you get a warning about `SQLALCHEMY_TRACK_MODIFICATIONS` it is ok.
```
>>> from fileName import db
>>> db.create_all()
```
## Styles
- Create a folder and add the following to your html to import styles
- 

- Coolors.co


## Dependencies
- Flask
  - https://flask.palletsprojects.com/en/1.1.x/
- Jinja
    - https://jinja.palletsprojects.com/en/2.11.x/
- Flask SQLAlchemy
  - https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- Flask Marshmallow
  - https://flask-marshmallow.readthedocs.io/en/latest/
- Marshmallow-sqlalchemy
  - https://marshmallow-sqlalchemy.readthedocs.io/en/latest/

