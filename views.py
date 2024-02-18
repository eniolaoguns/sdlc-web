from flask import Flask, render_template, redirect, url_for,Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models.createTable import User, ProductList, Account, Review, PaymentMethod, Product, DeliveryMethod, db, bcrypt

views = Blueprint(__name__,"views")

#individual pages rendering the flask to the html templates for the clothes and jewellery pages 
@views.route("/")
##links to the home index page
def home():
    return render_template('index.html')


@views.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@views.route("/addProduct", methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        description = request.form.get('description')
        tags = request.form.get('tags')
        stock_quantity = int(request.form.get('stock_quantity'))
        category = request.form.get('category')
        price = float(request.form.get('price'))
        discount = float(request.form.get('discount'))
        date_added = request.form.get('date_added')  
        image = request.form.get('image')

        # Create a new product
        new_product = Product(
            name=name,
            description=description,
            tags=tags,
            stock_quantity=stock_quantity,
            category=category,
            price=price,
            discount=discount,
            date_added=date_added,  
            image=image
        )

        # Add the product to the database
        db.session.add(new_product)
        db.session.commit()

        # Redirect to a success page or another route CHANGE THIS
        return redirect(url_for('views.success'))

    # Render the form for adding a product (GET request)
    return render_template('add_product.html')  # Replace with your actual template name




@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@views.route("/clothing", methods=['GET'])
def clothing():
    return render_template('clothing.html')

@views.route("/jewelry")
def jewelry():
    return render_template('jewelery.html')

@views.route("/basket")
def checkout():
    return render_template('checkout.html')


@views.route("/account")
def account(username):
    #allows the retrieval of the query parameters
    args = request.args
    name = args.get('name')
    return render_template('account.html', name=name)

@views.route("/checkout")
def checkout():
    return render_template('checkout.html')


@views.route("/category")
def categoryName(categoryName):
    args = request.args
    categoryName = args.get('categoryName')
    return render_template('category.html', category=categoryName)

@views.route("/Product Page/<int:product_id>")
def product(product_id):
    return render_template('productPage.html', product = product_id )

@views.route("/search?q=<query>")
def search(query):
    return render_template('search.html',search = query)


