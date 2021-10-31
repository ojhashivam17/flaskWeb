from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')
    #'Hello, World!'
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')



if __name__ == "__main__":
    app.run(debug=True,port=8000)