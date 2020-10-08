# pylint: disable=missing-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from src.models.models import Product

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

# if __name__ == "__main__":
