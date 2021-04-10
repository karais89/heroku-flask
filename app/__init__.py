# save this as app.py
from flask import Flask, escape, request


def create_app():
    app = Flask(__name__)

    @app.route("/api/hello")
    def hello():
        name = request.args.get("name", "World")
        return f"Hello, {escape(name)}!"

    return app