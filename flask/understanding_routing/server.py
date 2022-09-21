from flask import Flask


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string>')
def say_something(string):
    string = string.capitalize()
    return f"Hi {string}!"

@app.route('/repeat/<string:str>/<int:num>')
def repeat(str, num):
    return f'{str*num}'


if __name__=="__main__":
    app.run(debug=True)