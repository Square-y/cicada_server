from flask import Flask
from flask_pymongo import PyMongo
from config import conf


mongodb = PyMongo()


def create_app():
    app = Flask(__name__)
    app.config.from_object(conf)
    mongodb.init_app(app, uri='mongodb://192.168.85.129:27017/cicada')

    from .article import article_bp
    app.register_blueprint(article_bp)

    from .user import user_bp
    app.register_blueprint(user_bp)

    from .file import upload_bp
    app.register_blueprint(upload_bp)
    return app