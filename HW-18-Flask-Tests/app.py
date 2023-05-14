from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@db:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sadasdsdssadsadsadsadsadssaddas"

db.init_app(app)

with app.app_context():
    from routes import *
    from models import *

    migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)