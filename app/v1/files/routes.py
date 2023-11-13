import os
from flask import request
from app import app
from app.v1.files import bp

@bp.post("/")
def hello():
    file = request.files['file']
    # check file extension
    if not file.mimetype in app.config.get('ALLOWED_UPLOAD_FILES_EXTENSIONS'):
        return f'{file.mimetype} is not supported', 400
    path = request.form['path']
    folderPath = app.config.get('UPLOAD_FOLDER') + path
    existFolder = os.path.isdir(folderPath)
    fullPath = f'{folderPath}/{file.filename}'
    if not existFolder:
        os.makedirs(folderPath, exist_ok=True)
    if os.path.isfile(fullPath):
        return 'File is exist', 409
    file.save(os.path.join(folderPath, file.filename))
    response = dict(
        name = file.filename,
        path = folderPath,
        fullPath = fullPath
    )
    return response
