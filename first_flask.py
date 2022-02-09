from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Veeresh </h1>"

@app.route('/<name>')
def info(name):
    return '<h1> hi i am {},I am {} old '.format(name,'23')

@app.route('/info1')
def info1():
    return '<h1> hi i am {},I am {} old '.format('Naruto','23')

@app.route('/info/about')
def abour():
    return "<h1> The Lock-Down is going on<h1>"


if __name__ == '__main__':
    app.run("127.0.0.1",port=1234,debug=True)
