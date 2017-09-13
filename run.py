from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/Xiangwan')
def details():
	return render_template('A10119.html')

if __name__ == '__main__':
    app.run(debug=True)