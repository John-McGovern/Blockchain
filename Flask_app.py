
from flask import Flask, render_template, request, redirect
from blockchain_basis import Blockchain
#import web_blockchain_initalisation
import json

users = ["visibletitle", "kittdermis", "snowflakeshiver"]


online = Blockchain("online", users)

blockchain_app = Flask(__name__)

@blockchain_app.route("/", methods = ["GET","POST"])
def blockchain_page():
    created_block = None
    if len(request.form) > 0:
      form_from = request.form["from"]
      to = request.form["to"]
      data = request.form["block_add"]
      created_block = online.create_node(data, form_from, to)
    with open("online.json") as readable:
        message = json.load(readable)
    return render_template("Blockchain_template.html", message = message, app_name = "Blockchain", created_block = created_block, users = users)

@blockchain_app.route("/update", methods = ["GET","POST"])
def update_users_chain():
    with open("online.json") as readable:
        message = json.load(readable)
    #user_name = request.form["user_name"]
    return render_template("update.html", users = users)


#gives user a copy of the blockchain
@blockchain_app.route("/update/<user>")
def update_users_chain_page(user):
    with open("online.json") as readable:
        message = json.load(readable)
    return render_template("Block_to_add.html", users = user, message = message)
    