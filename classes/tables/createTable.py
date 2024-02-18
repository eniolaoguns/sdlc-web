from flask import Flask, render_template, redirect, url_for, request
from views import views
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WMGzon.db'
app.config['SECRET_KEY'] = 'wmgzon12345!'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Sets the view function that handles login requests. route or view function named 'login' that handles user login.
login_manager.login_view = 'login'

#this class serves the purpose of managing user sessions and loging in and out
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ProductList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

#this class contains all the general user details

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    permission_id = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Account('{self.username}', '{self.email}')"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)
    card_holder_name = db.Column(db.String(100), nullable=False)
    card_holder_expiry_date = db.Column(db.String(5), nullable=False)
    card_provider = db.Column(db.String(50), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    tags = db.Column(db.String(100))
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float)
    date_added = db.Column(db.DateTime, nullable=False)
    quantity_sold = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255))


class DeliveryMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line_1 = db.Column(db.String(255), nullable=False)
    address_line_2 = db.Column(db.String(255))
    address_line_3 = db.Column(db.String(255))
    address_city = db.Column(db.String(100), nullable=False)
    address_country = db.Column(db.String(100), nullable=False)
    address_postcode = db.Column(db.String(20), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


