from flask import jsonify, Response
from app import app
from flask_http_middleware import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self):
        super().__init__()


    def dispatch(self, request, call_next):
        if request.headers.get("token") != app.config.get('SECRET') and request.method != 'GET':
            return Response(response="Unauthorized", status=401)
        
        url = request.url
        response = call_next(request)
        response.headers.add("x-url", url)
        return response

    def error_handler(self, error):
        return jsonify({"error": str(error)})
    