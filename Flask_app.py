
from flask import Flask, render_template, request
from blockchain_basis import Blockchain

new = Blockchain("new")


blockchain_app = Flask(__name__)

@blockchain_app.route("/", methods=["GET", "POST"])
def blockchain_page():
    data_to_add = request.form["block_add"]
    if_block_made = new.create_node(data_to_add)
    return render_template("Blockchain_template.html", app_name = "Blockchain", if_block_made = if_block_made)

@blockchain_app.route("/add_block_output.html")
def add_block_output():
    return(render_template("add_block_output.html", block_added = "True", new_block_hash = "Test"))