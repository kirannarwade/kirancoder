from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/projects/Fully+Ecommerce+Website+(Flipkart+Clone)")
def ecommerce():
    return render_template("ecommerce.html")

@app.route("/projects/blog")
def blog():
    return render_template("blog.html")

@app.route("/projects/multi-todo")
def multi():
    return render_template("multi.html")

@app.route("/projects/todo")
def todo():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
