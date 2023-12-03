import os
from flask import request, jsonify, send_file
from app import app
from app.v1.files import bp
from marshmallow import Schema, fields, ValidationError

class UploadSchema(Schema):
    path = fields.String(required=True)

@bp.post("")
def upload():
    if 'file' not in request.files:
        return '', 400
    
    file = request.files['file']
    
    schema = UploadSchema()
    try:
        # Validate request body against schema data types
        schema.load(request.form)

        # # check file extension
        if not file.mimetype in app.config.get('ALLOWED_UPLOAD_FILES_EXTENSIONS'):
            return f'{file.mimetype} is not supported', 400
        
        if request.form['path'][0] != '/':
            return 'Path: first character is not - /', 400 
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400
    
    path = request.form['path']
    folderPath = app.config.get('UPLOAD_FOLDER') + path
    existFolder = os.path.isdir(folderPath)
    savedFullPath = f'{path}/{file.filename}'
    fullPath = f'{folderPath}/{file.filename}'

    if not existFolder:
        os.makedirs(folderPath, exist_ok=True)
    if os.path.isfile(fullPath):
        return 'File is exist', 409
    
    file.save(os.path.join(folderPath, file.filename))

    response = dict(
        name = file.filename,
        path = savedFullPath,
    )

    return response

@bp.delete("/<path:subPath>")
def delete(subPath):
    uploadFolder = app.config.get('UPLOAD_FOLDER')
    fullPath = f'{uploadFolder}/{subPath}'
    if not os.path.exists(fullPath):
        return 'File is not exist', 400
    os.remove(fullPath)
    return ''

@bp.get("/<path:subPath>")
def view(subPath):
    uploadFolder = app.config.get('UPLOAD_FOLDER')
    fullPath = f'{uploadFolder}/{subPath}'
    if not os.path.exists(fullPath):
        return 'File is not exist', 400
    print(os.path.dirname(app.instance_path) + fullPath)
    return send_file(f'{os.path.dirname(app.instance_path)}/{fullPath}')
