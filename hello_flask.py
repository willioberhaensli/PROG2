from flask import Flask
from flask import render_template

app = Flask("Hello World")



if __name__ == "__main__":
	app.run(debug=True, port=5000)