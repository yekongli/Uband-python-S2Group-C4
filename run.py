from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def details():
	return render_template('Qingya.html')

if __name__ == '__main__':
    app.run(debug=True)