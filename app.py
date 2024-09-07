from flask import Flask,render_template, request
from Mlops.Pipelines.test import Custom_data, Predict_Pipeline
import pandas as pd


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
        df = pd.read_csv('artifacts/accuracy_report.csv')
        print("Regression onlu ",df['Linear Regression'],"\n",df['XG Boost'])
        return render_template('Output.html',results = result[0],r2_linear_regression = df['Linear Regression'][0]  ,r2_xg_boost = df['XG Boost'][0] , r2_ada_boost = df['Ada Boost'][0], r2_decision_tree =df['Decision Tree Regressor'][0] ,r2_random_forest= df['Random Forest Regressor'][0] ,r2_gradient_boosting = df['Gradient Boosting'][0])
        

if __name__ == '__main__':
    app.run(debug=True)
