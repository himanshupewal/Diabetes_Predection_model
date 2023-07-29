# Diabetes Prediction using Logistic Regression


![diabetes](https://github.com/himanshupewal/Diabetes_Predection_model/assets/84642624/ffa92adb-0e74-4642-8342-d0fa835c7d93)


## Overview
<!-- Add a brief project description -->
This repository contains a diabetes prediction model using logistic regression. The goal of this project is to predict whether an individual has diabetes or not based on various input features such as age, BMI, glucose levels, blood pressure, and other relevant attributes.

## Table of Contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Contact](#contact)

## Dataset

The dataset used for this project can be found in the [kaggle/](Diabetes_Dataset/) directory. It includes information about individuals, such as age, BMI, glucose levels, blood pressure, and other relevant attributes. The target variable, "Diabetes_Status," indicates whether each individual has diabetes or not (0 for non-diabetic, 1 for diabetic).

The dataset is sourced from [data-source-url](https://www.kaggle.com/datasets/mathchi/diabetes-data-set), and it has been preprocessed to handle missing values, outliers, and ensure data quality.

## Installation

  To run this project locally, follow these steps:
  
      1. Clone this repository to your local machine: git clone https://github.com/himanshupewal/diabetes-prediction.git
      
      ## Navigate to the Project Directory
      
      To run this project locally, you'll need to navigate to the project directory on your computer. Follow the steps below to do so:
      
      1. First, clone this repository to your local machine by executing the following command in your terminal or command prompt:
      
      
      2. Once the cloning process is complete, change your current working directory to the "diabetes-prediction" directory (the name of the project directory) using the `cd` command:
      
      
      3. You are now inside the project directory, and you can proceed with the installation and usage instructions mentioned in the README.md file.
      
      
      This command will install the necessary dependencies for the project.
      
      4. Now, you're ready to explore the project, run the Jupyter Notebook, and work with the diabetes prediction model.
    
      If you encounter any issues during the installation process or have any questions, feel free to reach out for assistance.




## Install the required dependencies:
    pip install -r requirements.txt



## Usage

1. Open and run the Jupyter Notebook [notebooks/Diabetes_Prediction.ipynb](notebooks/Diabetes_Prediction.ipynb) to explore the dataset, preprocess the data, train the logistic regression model, and evaluate its performance.

2. Modify the notebook as needed for hyperparameter tuning and other experiments.

3. To make predictions on new data, use the provided [predict.py](predict.py) script, which takes the input features as command-line arguments and outputs the predicted diabetes status.

## Model Evaluation

  The performance of the diabetes prediction model is evaluated using metrics such as:
  
  - Accuracy: The proportion of correctly predicted instances out of the total instances.
  - Precision: The proportion of true positive predictions out of all positive predictions.
  - Recall: The proportion of true positive predictions out of all actual positive instances.
  - F1 Score: The harmonic mean of precision and recall, providing a balanced metric.

  The evaluation results can be found in [results/evaluation_metrics.txt](results/evaluation_metrics.txt).

## Results

The diabetes prediction model achieved promising results with an accuracy of 75.5%, precision of 74%, recall of 75%, and F1 score of 75%.





   

