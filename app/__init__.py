import os
from flask import Flask, send_from_directory

def create_app():
    # Use absolute path for static_folder to ensure it works on Vercel
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(base_dir, '..', 'public')
    app = Flask(__name__, static_folder=static_folder, static_url_path='')
    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    return app

app = create_app()
