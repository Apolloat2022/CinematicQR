from flask import Flask, send_from_directory

def create_app():
    app = Flask(__name__, static_folder='../public', static_url_path='')
    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    return app

app = create_app()
