from flask import Flask

from scores import pages


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app
