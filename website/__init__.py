from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jkdjaskeqwjklji38921u8uj#*(Yhu13'

    return app