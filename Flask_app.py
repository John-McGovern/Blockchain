
from flask import Flask

blockchain_app = Flask(__name__)

@blockchain_app.route("/")
def blockchain_page():
    return"Hello World"