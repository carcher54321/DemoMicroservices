from flask import Blueprint

hospital_api_blueprint = Blueprint('user-api', __name__)

from . import routes
