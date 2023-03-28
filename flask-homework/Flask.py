from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "Information about us"


@app.route('/contact')
def contact():
    return "Our contact +380123456789 go to URL: https://"

if __name__ == '__main__':
    app.run()