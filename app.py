from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('index.html')
    #'Hello, World!'
@app.route('/')
def home():
    return 'Welcome to Test Academy'

if __name__ == "__main__":
    app.run(debug=True,port=8000)