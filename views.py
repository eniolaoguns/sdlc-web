from flask import Flask, render_template, Blueprint, request, jsonify

views = Blueprint(__name__,"views")

#individual pages rendering the flask to the html templates for the clothes and jewellery pages 
@views.route("/")
##links to the home index page
def home():
    return render_template('index.html')


@views.route("/login")
def login():
    return render_template('login.html')

@views.route("/signup")
def signup():
    return render_template('signup.html')

@views.route("/clothing")
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





