
from flask import Flask, render_template



blockchain_app = Flask(__name__)

@blockchain_app.route("/")
def blockchain_page():
    return render_template("Blockchain_template.html", app_name = "Blockchain")