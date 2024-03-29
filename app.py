from flask import Flask, render_template
from views import views
from flask_sqlalchemy import SQLAlchemy

#initallises the application
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)