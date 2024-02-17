from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

##check the location here
def home():
    return render_template('index.html')
iiug
def hello():
    return 'Hello,World'

if __name__ == '__main__':
    app.run(debug=True)