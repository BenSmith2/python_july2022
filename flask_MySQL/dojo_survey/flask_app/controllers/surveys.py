from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.survey import Survey

@app.route('/')
def display_survey():
    return render_template('survey_page.html')


@app.route('/survey_handle', methods=['POST'])
def survey_handle():
    data = {
        'name': request.form['name'],
        'dojo_location': request.form['dojo_location'], 
        'favorite_language': request.form['favorite_language'], 
        'comments': request.form['comments']
    }
    if not Survey.validate_survey(data):
        return redirect('/')
    
    Survey.add_survey(data)

    return redirect('/result')

@app.route('/result')
def result_survey():
    
    survey = Survey.result()

    return render_template('result_survey.html', survey = survey)
