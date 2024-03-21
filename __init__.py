from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Application factory function
def create_app():
    # App instance
    app = Flask(__name__)
    app.config.from_object('config.config')

    # Importing and registering models
    from app.models.users import User
    from app.models.companies import Company
    from app.models.books import Book

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return "Authors API Project setup 1"

    return app

# This conditional block allows you to run the Flask app when this script is executed
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
