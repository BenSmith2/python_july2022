from flask import Flask, render_template
app=Flask(__name__)

@app.route('/<int:num>')
def success(num):
    return render_template("index.html",num = num)
@app.route('/<int:num>/<string:color>')
def with_color(num,color):
    return render_template("index.html",num = num,color = color)

if __name__=="__main__":
    app.run(debug=True)