
from flask import Flask, render_template, request
from blockchain_basis import Blockchain

new = Blockchain("new")


blockchain_app = Flask(__name__)

@blockchain_app.route("/", methods = ["GET","POST"])
def blockchain_page():
    created_block = None
    if len(request.form) > 0:
      data = request.form["block_add"]
      
    return render_template("Blockchain_template.html", app_name = "Blockchain", created_block = created_block)

@blockchain_app.route("/add_block_output.html")
def add_block_output():
    return(render_template("add_block_output.html", block_added = "True", new_block_hash = "Test"))