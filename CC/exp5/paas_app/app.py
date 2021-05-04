from flask import Flask, render_template, url_for, request, session, redirect, flash

app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = "ursecretkey"

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
