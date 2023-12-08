import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = False
    UPLOAD_FOLDER = 'files'
    ALLOWED_UPLOAD_FILES_EXTENSIONS = {'text/plain', 'application/pdf', 'image/png', 'image/jpeg', 'image/gif'}
    SECRET = 'ASD1902dj()ASDJasd;-safds'

class DevelopementConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    UPLOAD_FOLDER = 'files'
    DEBUG = True

class ProductionConfig(BaseConfig):
    UPLOAD_FOLDER = 'files'
    DEBUG = False
