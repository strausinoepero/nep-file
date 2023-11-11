import os
from flask import request
from app import app
from app.v1.files import bp

@bp.post("/")
def hello():
    files = request.files['file']
    path = request.form['path']
    folderPath = app.config.get('UPLOAD_FOLDER') + path
    existFolder = os.path.isdir(folderPath)
    fullPath = f'{folderPath}/{files.filename}'
    if not existFolder:
        os.makedirs(folderPath, exist_ok=True)
    if os.path.isfile(fullPath):
        return 'File is exist', 409
    files.save(os.path.join(folderPath, files.filename))
    response = dict(
        name = files.filename,
        path = folderPath,
        fullPath = fullPath
    )
    return response
