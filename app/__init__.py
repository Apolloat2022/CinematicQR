import os
from flask import Flask, send_from_directory

def create_app():
    app = Flask(__name__)
    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app

app = create_app()
