
from flask import Flask, render_template, request, redirect, url_for
from backend.app.controllers import product_controller, auth_controller

app = Flask(__name__)

# Register Blueprints for organization
app.register_blueprint(product_controller.blueprint)
app.register_blueprint(auth_controller.blueprint)

@app.route('/')
def index():
    return render_template('cupcakes.html')

if __name__ == "__main__":
    app.run(debug=True)
