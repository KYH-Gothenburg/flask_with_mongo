from flask import Flask, render_template
from db.models import User, Product

app = Flask(__name__)


@app.get('/')
def index():
    users = User.all()
    products = Product.all()
    return render_template('index.html', users=users, products=products)


if __name__ == '__main__':
    app.run()
