"""""""""""""""""""""""""""
OBC Lecture 12 - Supervised Learning Example
Classification with Logistic Regression
Pima Indians Diabetes
7/29/25

This script performs logistic regression using the Pima Indians Diabetes dataset.

Data source: Pima Indians Diabetes Dataset from Kaggle
https://www.kaggle.com/datasets/gzdekzlkaya/pima-indians-diabetes-dataset?resource=download

Dataset Overview:
Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skinfold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index
DiabetesPedigreeFunction: Diabetes likelihood based on family history
Age: Age in years
Outcome: Diabetes diagnosis result (1 = positive, 0 = negative)
"""""""""""""""""""""""""""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


"""
Values
"""
INPUT_FILENAME = "pima_diabetes_data.csv"
OUTCOME_COL_NAME = "Outcome"
RANDOM_SEED = 5


"""
Import data as pandas DataFrame and Split into Features (X) and Target (y)
"""
data = pd.read_csv(INPUT_FILENAME)

# Set features and target
X = data.drop(columns=[OUTCOME_COL_NAME])
y = data[OUTCOME_COL_NAME]


"""
Split Dataset into Training and Testing Sets
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)


"""
Train the Logistic Regression Model
"""
# Initialize the model
model = LogisticRegression(
    penalty='l2',
    solver='liblinear',
    max_iter=1000
)

# Model training
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)


# Model Evaluation
accuracy_train = model.score(X_train, y_train)
print("Accuracy (train):", accuracy_train)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy (test):", accuracy)
print("")