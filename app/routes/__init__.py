from flask import Flask
from app.routes.register_series_route import bp as bp_register

def init_app(app: Flask):
    app.register_blueprint(bp_register)