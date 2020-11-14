
from flask import Flask, render_template, request
from blockchain_basis import Blockchain

online = Blockchain("online")


blockchain_app = Flask(__name__)

@blockchain_app.route("/", methods = ["GET","POST"])
def blockchain_page():
    created_block = None
    if len(request.form) > 0:
      form_from = request.form["from"]
      to = request.form["to"]
      data = request.form["block_add"]
      print(form_from, to, data)
      created_block = online.create_node(data, form_from, to)
      #with open("online.json") as readable:
            #message = json.load(readable)
            #print(message)
    return render_template("Blockchain_template.html", app_name = "Blockchain", created_block = created_block)

#not_needed
@blockchain_app.route("/add_block_output.html")
def add_block_output():
    return(render_template("add_block_output.html", block_added = "True", new_block_hash = "Test"))