
from flask import Flask, render_template, request, redirect
from blockchain_basis import Blockchain
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
#import web_blockchain_initalisation
import json

users = ["visibletitle", "kittdermis", "snowflakeshiver"]

users_dict = {"visibletitle":"visibletitle", "kittdermis": "kittdermis", "snowflakeshiver": "snowflakeshiver"} 

online = Blockchain("online", users)


blockchain_app = Flask(__name__)
blockchain_app.config["SECRET_KEY"] = "my_secret"

class CreateBlockForm(FlaskForm):
    data = StringField("Enter Data:", validators = [DataRequired()])
    sender = SelectField("Sender:", choices = users_dict, validators = [DataRequired()])
    receiver = SelectField("Receiver:", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("submit")

class UpdateForm(FlaskForm):
    comment = StringField("comment", validators = [DataRequired()])
    select = SelectField("select", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("submit")

class SearchForm(FlaskForm):
    user = SelectField("User:", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("submit", validators = [DataRequired()])

@blockchain_app.route("/", methods = ["GET","POST"])
def blockchain_page():
    create_block_form = CreateBlockForm()
    created_block = None
    
    form_from = create_block_form.sender.data
    to = create_block_form.receiver.data
    data = create_block_form.data.data
    create_submit = create_block_form.submit.data
    if create_submit:
        print("a")
    if data:
        created_block = online.create_node(data, form_from, to)
    with open("online.json") as readable:
          message = json.load(readable)
    
    return render_template("Blockchain_template.html", message = message, app_name = "Blockchain", created_block = created_block, users = users, create_block_form = create_block_form )

#route where users can get copies of the chain
@blockchain_app.route("/update", methods = ["GET","POST"])
def update_users_chain():
    with open("online.json") as readable:
        message = json.load(readable)
    #user_name = request.form["user_name"]
    update_form = UpdateForm()
    update_submit = update_form.submit.data
    update_user = update_form.select.data
    if update_submit:
        return redirect(f"/update/{update_user}")
    return render_template("update.html", users = users, update_form = update_form)


#gives user a copy of the blockchain
@blockchain_app.route("/update/<user>")
def update_users_chain_page(user):
    with open("online.json") as readable:
        message = json.load(readable)
    return render_template("Block_to_add.html", users = user, message = message)

#route where transactions can be searched for sender and receiver
@blockchain_app.route("/search", methods = ["GET","POST"])
def search_chain():
    search_form = SearchForm()
    user = search_form.user.data
    submit = search_form.submit.data
    user_transactions = online.users_transactions(user)
    
    return render_template("Search.html", search_form= search_form, submit = submit, user_transactions = user_transactions, user = user)

@blockchain_app.route("/home", methods = ["GET","POST"])
def home():
    return render_template("home.html")