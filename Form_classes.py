#This file contatins all the Formclasses (derived from FlaskForm) that are used in the web app.
#It also contains a list of randomly generated usernames, that are used through the web app.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

users_dict = {"visibletitle":"visibletitle", "kittdermis": "kittdermis", "snowflakeshiver": "snowflakeshiver"} 


#creates a form that gathers the sender, reciever and data in a transaction
class CreateBlockForm(FlaskForm):
    data = StringField("Enter Data:", validators = [DataRequired()])
    sender = SelectField("Sender:", choices = users_dict, validators = [DataRequired()])
    receiver = SelectField("Receiver:", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("Submit", validators = [DataRequired()])

#Creates a form for a user to generate the data for a personal page which shows the full blockchain
class UpdateForm(FlaskForm):
    comment = StringField("Comment", validators = [DataRequired()])
    select = SelectField("Select:", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("Submit:", validators = [DataRequired()])

#Creates a form that gathers a username so that all the transactions of that user can be shown
class SearchForm(FlaskForm):
    user = SelectField("User:", choices = users_dict, validators = [DataRequired()])
    submit = SubmitField("Submit:", validators = [DataRequired()])