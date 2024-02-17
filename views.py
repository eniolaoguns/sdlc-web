from flask import Flask, render_template, Blueprint

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
def account():
    return render_template('account.html')

@views.route("/checkout")
def checkout():
    return render_template('checkout.html')

#commenteed these out for now to come back to 
#@views.route("/category/<category_name>")
#@views.route("/Clothing and Jewelery/<int:product_id>")
#@views.route("/search?q=<query>")





