from flask import flask
app = Flask("Hello World")
@app.route('/Hello') 
def hello_world():
	return'Hello, World!'

	if __name__ == "__main__":
		app.run(debug=True, port=5000)

