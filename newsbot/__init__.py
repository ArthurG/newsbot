from flask import Flask
from flask_sqlalchemy iomport SQLAlchemy
from .webhook import webhook
from .profile import profile

newsbot = Flask (__name__)
newsbot.register_blueprint(webhook)
newsbot.register_blueprint(profile)

db = SQLAlchemy(newsbot)
