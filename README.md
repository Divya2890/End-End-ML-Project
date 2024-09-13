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
1. Logistic regression
2. XG-Boost
3. Ada boost
4. Decision Tree regression
5. Random Forest regression
6. Gradient Boosting
 and uses GridsearchCV for hyperparameter optimisation and saves the model weights with best R2_score in the pickle file.

### 4. **🗂️ Pipeline **
Once the components are built and the pickle files are created, we move on to creating a **pipeline folder**. This folder is designed to:

- 📂 Load the processor.pkl to apply transformation on test data
- 📊 Load the model.pkl file to get the predictions for test data.

This pipeline automates the process of transforming new incoming data and making predictions using the best-trained model.


### 5. **🌐 Building a Flask App**
After training the models and setting up the pipeline, we create a **Flask** web application that allows:

- 🔗 Users to send new data to the model through API endpoints.
- 🧮 The app to process the incoming data using the transformation pipeline and return predictions from the trained model.

### 6. **☁️ Deploying to EC2 and CI/CD Pipeline**
Finally, the project involves deploying the model and Flask app to production environments:

- **EC2 Deployment**: The trained model and Flask app are deployed on an AWS EC2 instance to make the service publicly available.
- **CI/CD Pipelines**: A continuous integration/continuous deployment (CI/CD) pipeline is set up using GitHub Actions or other tools to automate the deployment process and ensure seamless updates to the app and model.

## 📦 Key Project Outputs

- **Pickle files**: `.pkl` files for the data processing pipeline and the best-trained model.
- **Pipeline folder**: A pipeline folder that automates data transformation and prediction.
- **Flask app**: An API that exposes endpoints to receive new data and return predictions.
- **EC2 Deployment**: The app and model are hosted on an EC2 instance, with a CI/CD pipeline for continuous updates.

---

This modular approach to building, transforming, and deploying machine learning models ensures efficiency and scalability. The use of pickle files and pipelines enables automation for consistent predictions across different data inputs, while Flask and EC2 provide a robust solution for serving the model.




# End-End-ML-Project

# 5 Steps of ML pipelines will be discussed and presented
1. Data Ingestion
2. Data transformation
3. Model Training
4. Model Deployment 
5. Model Monitoring 

Moreover, we use a setup.py file to import this ML project as a package that is easily transferable and be used by anyone without having to go through the need of worrying to install the prerequiste packages.

# Steps followed 

Step 1: Created a conda environment using conda create -p ./Mlops python = 3.8
Step 2: Create a file called Requirements.txt which contains the list of all the packages needed for this project 
Step 3: Create a setup.py file which uses the Requirements.txt to install the packages and also initiate the meta data of the package created for the python project.

Note: we use a setup() main function to initialise the metadata of the package. 
``` install_requires = [] # specify the dependencies of the project i.e. required packages using pip. Instead of specifying them as a list, we can call a function that picks up the list from the Requirements.txt```
``` packages = find_packages() # find_packages is an inbuilt function from setuptools that searches the entire project folder to find the init files and install all the dependecies. More useful when you create multiple packages in the project. ```
