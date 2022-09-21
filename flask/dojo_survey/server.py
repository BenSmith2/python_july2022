from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'assdfdohdxcsawswerfinvoiesdfnwercssdlsddhfkvjnsldkcafmi'


@app.route('/')
def registration_page():
    return render_template('index.html')

@app.route('/handle', methods=['POST'])
def handle():
    session['fname']=request.form['first_name']
    session['loca']=request.form['location']
    session['lang']=request.form['language']
    return redirect('/user_info')

@app.route('/user_info')
def show_info():
    return render_template('user_info.html')


if __name__=="__main__":
    app.run(debug=True)