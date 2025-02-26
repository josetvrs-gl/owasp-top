from flask import Flask, session
from app.routes.auth import auth
from app.routes.users import users
from app.routes.index import index
from app.routes.ping import ping
from app.routes.cards import cards
from app.db import init_db

init_db()

def create_app():
    app = Flask(__name__, template_folder='app/templates')
    app.secret_key = "oc856vw8965wn4f57o82c5v285"
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(ping, url_prefix='/ping')
    app.register_blueprint(cards, url_prefix='/cards')
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
