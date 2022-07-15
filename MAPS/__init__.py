from sqlite3 import Connection as SQLite3Connection
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime
from flask_googlemaps import Map, icons, GoogleMaps

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Virtual_Market.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQL_TRACK_MODIFICATION'] = 0

# you can set key as config
app.config["GOOGLEMAPS_KEY"] = "AIzaSyAoGRheGae8InAbLntpC0oKV_NP63KnroY"
GoogleMaps(app, key="AIzaSyAoGRheGae8InAbLntpC0oKV_NP63KnroY")


# configure SQLITE3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from MAPS import routes