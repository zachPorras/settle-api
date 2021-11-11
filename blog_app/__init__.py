from flask import Flask
from config import Config
from .authentication.routes import auth
from .api.routes import api
from .site.routes import site
from .models import db, login_manager, ma
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)