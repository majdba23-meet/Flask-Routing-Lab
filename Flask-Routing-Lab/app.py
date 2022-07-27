from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home():
    return render_template("home.html")



@app.route('/product')
def product():
    return render_template("product.html")

@app.route('/p2')
def p2():
    return render_template("p2.html")

@app.route('/p3')
def p3():
    return render_template("p3.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route('/cart2')
def cart2():
    return render_template("cart2.html")


@app.route('/cart3')
def cart3():
    return render_template("cart3.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
