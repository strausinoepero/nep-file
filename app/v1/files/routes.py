import os
from flask import request
from app import app
from app.v1.files import bp

MAX_FILE_SIZE = 8 * 1024 * 1024 + 1


@bp.post("/")
def hello():
    files = request.files['file']
    path = request.form['path']
    folderPath = app.config.get('UPLOAD_FOLDER') + path
    existFolder = os.path.isdir(folderPath)
    fullPath = f'{folderPath}/{files.filename}'
    filenameNotExtension, fileExtension = os.path.splitext(files.filename)
    listExtension = app.config.get('ALLOWED_UPLOAD_FILES_EXTENSIONS')
    mimetype = files.mimetype
    fileBytes = files.read(MAX_FILE_SIZE)
    print('ddfmd', len(fileBytes))
    if len(fileBytes) == MAX_FILE_SIZE:
        return f'file size exceeds {MAX_FILE_SIZE} byte', 409
    if not mimetype in listExtension:
        return f'files with the extension {mimetype} are not supported', 409
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
