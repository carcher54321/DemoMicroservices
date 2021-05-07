from flask import Blueprint

surgery_api_blueprint = Blueprint('user-api', __name__)

from . import routes
