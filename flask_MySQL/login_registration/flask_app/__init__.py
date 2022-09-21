from flask import Flask, session
import re

app = Flask(__name__)
app.secret_key = "nbirmpmsvpinwpecnxpmvorpnonqdoinvonownfiuvbudyfbmr0]9fweuovnb"

DATABASE = "login_validation_practice"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')