import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)