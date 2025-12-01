from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("stress_classifier_model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    message = None
    alert_type = None

    if request.method == 'POST':
        anxiety_level = int(request.form['anxiety_level'])
        self_esteem = int(request.form['self_esteem'])
        mental_health_history = int(request.form['mental_health_history'])
        depression = int(request.form['depression'])
        headache = int(request.form['headache'])
        blood_pressure = int(request.form['blood_pressure'])
        sleep_quality = int(request.form['sleep_quality'])
        breathing_problem = int(request.form['breathing_problem'])
        noise_level = int(request.form['noise_level'])
        living_conditions = int(request.form['living_conditions'])
        safety = int(request.form['safety'])
        basic_needs = int(request.form['basic_needs'])
        academic_performance = int(request.form['academic_performance'])
        study_load = int(request.form['study_load'])
        teacher_student_relationship = int(request.form['teacher_student_relationship'])
        future_career_concerns = int(request.form['future_career_concerns'])
        social_support = int(request.form['social_support'])
        extracurricular_activities = int(request.form['extracurricular_activities'])

        data = [[anxiety_level, self_esteem, mental_health_history, depression, headache,
                 blood_pressure, sleep_quality, breathing_problem, noise_level, living_conditions,
                 safety, basic_needs, academic_performance, study_load, teacher_student_relationship,
                 future_career_concerns, social_support, extracurricular_activities]]

        p = int(model.predict(data)[0])

        if p == 0:
            prediction = "Low Stress"
            message = "Yay! Take it easy 🎉"
            alert_type = "success"
        elif p == 1:
            prediction = "Moderate Stress"
            message = "Take a deep breath 😌"
            alert_type = "warning"
        else:
            prediction = "High Stress"
            message = "Time to relax ❤️"
            alert_type = "danger"

    return render_template('index.html', prediction=prediction, message=message, alert_type=alert_type)

if __name__ == '__main__':
    app.run(debug=True)