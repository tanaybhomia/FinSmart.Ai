from flask import Flask

def create_app():
    app = Flask(__name__,static_folder='static')
    app.config['SECRET_KEY'] = 'hlkhvlkshvl'
    
    from .views import view  # Import 'view' blueprint, not 'views'
    from .auth import auth

    app.register_blueprint(view)  # Register 'view' blueprint, not 'views'
    app.register_blueprint(auth)
    return app
