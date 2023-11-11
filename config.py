import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = False
    UPLOAD_FOLDER = 'files'
    ALLOWED_UPLOAD_FILES_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class DevelopementConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    UPLOAD_FOLDER = '/srv/s4'
    DEBUG = True

class ProductionConfig(BaseConfig):
    UPLOAD_FOLDER = '/srv/s4'
    DEBUG = False
