from flask import Flask,render_template, request
from Mlops.Pipelines.test import Custom_data, Predict_Pipeline

# creating a instance of flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_score', methods=["POST", "GET"])
def predict_score():
    if request.method == "GET":
        return render_template('predict_form.html')
    else:
        form_data = Custom_data(gender=request.form.get('gender'),
        race_ethnicity=request.form.get('ethnicity'),
        parental_level_of_education=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('writing_score')),
        writing_score=float(request.form.get('reading_score')) )
        sample  = form_data.convert_to_dataframe()
        print(type(sample), sample,"TESTING MY SAMPLE DATAFRAME")
        result = Predict_Pipeline().predict_sample(sample)
        return render_template('predict_form.html', results = result[0])

if __name__ == '__main__':
    app.run(debug=True)
