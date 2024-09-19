# 🚀 Machine Learning Model Pipeline and Deployment

A beginner-level project to learn how to use a modular approach for building machine learning models to improve efficiency and scalability.

## 🛠️ Project Workflow

Initially, We first build components for the three core stages of the machine learning pipeline:

### 1. **📥 Data Ingestion**
Before building the components, we need to ingest the data. This includes:

- 🔍 Extracting and preparing the data for the transformation and model training stages.
-  Data can be obtained from various sources like CSV files, scraped from web, UCI repository, kaggle etc
- `Data_ingestion.py` reads out input data extracted from csv file and creates a train and test files and saves them to artifacts folder ( this is storage space for all the files required for the project ) 

### 2. **🔄 Data Transformation**
Key Tasks invoved in this step are

-  Imputing missing values
-  Applying Standard scaling
-  Discarding highly collinear columns
-  Performing PCA or adding new features to the data depending on the complexity of the dataset

`data_tranformation.py` is used to create a preprocessor.pkl file which can be used to apply the processing steps used for training the model on the test data
  
### 3. **🎯 Model Training**
The training stage involves:

- 🤖 Training multiple models using the transformed data.
- 📈 Performing hyperparamter tuning and evaluating all the models on test data
- 💾 Saving the best-performing model as a best_model.pkl file under artificats

`model_training.py` file in this project compares the following models

1. **Logistic regression**
2. **XG-Boost**
3. **Ada boost**
4. **Decision Tree regression**
5. **Random Forest regression**
6. **Gradient Boosting**

and uses GridsearchCV for hyperparameter optimisation and saves the model weights with best R2_score in the pickle file.

### 4. **🗂️ Pipeline **
Once the components are built and the pickle files are created, we move on to creating a **pipeline folder**. This folder is designed to:

- 📂 Load the processor.pkl to apply transformation on test data
- 📊 Load the model.pkl file to get the predictions for test data.

This pipeline automates the process of transforming new incoming data and making predictions using the best-trained model.


### 5. **🌐 Building a Flask App**
After training the models and setting up the pipeline, we create a **Flask** web application using `app.py` that allows:

- 🔗 Users to send new data to the model through post call submitted through a form from the app.
- 🧮 The app to process the incoming data using the transformation pipeline and return predictions from the trained model.

Check out the `input_form.png` and `prediction_result.png` for how the app looks and the results generated 

---

This modular approach to building, transforming, and deploying machine learning models ensures efficiency and scalability. The use of pickle files and pipelines enables automation for consistent predictions across different data inputs using a Flask application.

## 🔗 Extending Deployment to AWS or Azure Cloud ( Coming Soon )

While this project demonstrates hosting a Flask app, you can extend the project structure to deploy the machine learning model on AWS or Azure cloud platforms. Below is a quick overview of how to achieve this using AWS services.

## Approach 1
1. Build docker containers that includes your model, dependencies, and a web server (e.g., Flask) to handle predictions
2. Save the docker image to ECR (Elastic Container Registry ) if we wanted the model and data to be private
3. Use Elastic bean to host our Docker image and use the flask app through a public url.

## Approach 2
1. Upload our model to Amazon S3 (object storage service).
2. Create a SageMaker model object anf Configure an endpoint.
3. Deploy the model to the endpoint and use the endpoint to get our predicitons for the test data.


## References

[Modular Approach videos](https://www.youtube.com/watch?v=S_F_c9e2bz4&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG)



