import os
from flask import Flask, send_from_directory

def create_app():
    # Vercel's structure usually places the root at /var/task
    # We use a path relative to this file to find 'public'
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_folder = os.path.join(root_dir, 'public')
    app = Flask(__name__, static_folder=static_folder, static_url_path='')
    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    return app

app = create_app()
