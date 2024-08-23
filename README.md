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