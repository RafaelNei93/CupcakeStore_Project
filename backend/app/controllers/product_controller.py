
from flask import Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint('product', __name__, url_prefix='/product')

@blueprint.route('/')
def list_products():
    # Fetch and display products
    return render_template('cupcakes.html')

@blueprint.route('/add', methods=['POST'])
def add_product():
    # Logic to add product goes here
    return redirect(url_for('product.list_products'))
