from flask import Flask
from .webhook import webhook
from .profile import profile

newsbot = Flask (__name__)
newsbot.register_blueprint(webhook)
newsbot.register_blueprint(profile)


