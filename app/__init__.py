import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

from app.v1.files import bp as files_bp

app.register_blueprint(files_bp, url_prefix="/api/v1/files")
