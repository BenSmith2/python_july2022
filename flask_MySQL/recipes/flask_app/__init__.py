from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "kakjbiiejhvlknvwon97834067259-gfoniweiluqhr49898tv47onsvethn9"

DATABASE = "recipes"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')