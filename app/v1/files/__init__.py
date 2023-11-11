from flask import Blueprint

bp = Blueprint("/api/v1/files", __name__)

from app.v1.files import routes