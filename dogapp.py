import os
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

if "DOG_ENV" in os.environ:
    DOGTAG = "https://dog-years.herokuapp.com"
else:
    DOGTAG = "http://localhost:5000"


@app.route('/', methods=['GET'])
def home():
    if request.method == "GET":
        return render_template('homepage.html', addy = DOGTAG)

@app.route('/calc', methods=['POST'])
def calc_dog_years():
    dage = request.form['years']
    dog_age = int(dage) * 7

    return render_template('dogyears.html', addy = DOGTAG, age = dog_age)
if __name__ == '__main__':

   app.run()
