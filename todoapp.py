from flask import Flask
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hong:hong94@localhost/todo'

from views import *


if __name__ == '__main__':
    app.run()