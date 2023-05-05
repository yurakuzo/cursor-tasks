from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:yurakuzo2003@localhost:3306/flask"

app.secret_key = "sadasdsdssadsadsadsadsadssaddas"

db.init_app(app)

with app.app_context():
    from routes import *
    from models import User, Post

    migrate = Migrate(app, db)

if __name__ == "__main__":
    # from models import User, Post
    # db.session.query(User).delete()
    # db.session.query(Post).delete()
    # db.session.commit()
    app.run(host="0.0.0.0", port=5050, debug=True)