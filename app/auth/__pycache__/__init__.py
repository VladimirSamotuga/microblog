from flask import Blueprint

bp = Blueprint('authentication', __name__)

from app.auth import routes, forms