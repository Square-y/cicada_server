from flask import Blueprint

article_bp = Blueprint('articles', __name__, url_prefix="/articles")

from . import views