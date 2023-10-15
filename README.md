# Predicting Boston Housing Prices: A Machine Learning Approach

## Project Overview
Welcome to an exploration journey through the Boston Housing Prices dataset! <br>
This project unleashes the power of various machine learning models to predict housing prices with a dash of explorative data analysis, model interpretation, and application building.

📈 Highlights:
* In-depth Data Analysis: Comprehensive exploration of data to unveil underlying patterns and insights.
* Advanced Predictive Modeling: Deployment and evaluation of sophisticated models to predict housing prices with high precision.
* Model Interpretation: Employing SHAP values to provide transparent and interpretable model predictions.
* Interactive Application Development: Implementation of a Flask application, providing a user interface for real-time price predictions.

📦BostonHousingAnalysis
 ┣ 📂data
 ┃ ┗ 📜BostonHousing.csv
 ┣ 📂models
 ┃ ┗ 📜best_xgboost_model.pkl
 ┃ ┗ 📜data_scaler.pkl
 ┣ 📂notebooks
 ┃ ┗ 📜[All Notebooks]
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📂static
 ┃ ┗ 📜[ static files used in Flask app]
 ┣ 📜app.py
 ┗ 📜README.md
🔍 What's Inside:

* /data: Holds the foundational Boston Housing dataset.
* /models: Safeguards the trained machine learning models and data scalers.
* /notebooks: A collection of Jupyter notebooks detailing every step of the analysis and modeling process.
* /templates: HTML templates to render the Flask app.
* app.py: The script that brings the Flask app to life.
* README.md: Your guide through this project - the document you're reading right now!

# Introduction to the Boston Housing Dataset
The Boston Housing dataset, a cornerstone in the machine learning community, serves as a playground for aspiring data scientists and seasoned professionals alike to develop, experiment, and validate predictive models. Originating from the U.S Census Service, the dataset has been widely utilized in numerous studies and competitions, offering a rich and compact source of information for predictive analytics.

## Dataset Attributes
The dataset encapsulates 506 instances, each with the following attributes that describe various aspects of the housing conditions in Boston suburbs:

* CRIM: Per capita crime rate by town.
* ZN: Proportion of residential land zoned for large lots.
* INDUS: Proportion of non-retail business acres per town.
* CHAS: Charles River dummy variable (equals 1 if tract bounds river; 0 otherwise).
* NOX: Nitrogen oxide concentration (parts per 10 million).
* RM: Average number of rooms per dwelling.
* AGE: Proportion of owner-occupied units built prior to 1940.
* DIS: Weighted distances to five Boston employment centers.
* RAD: Index of accessibility to radial highways.
* TAX: Full-value property tax rate per $10,000.
* PTRATIO: Pupil-teacher ratio by town.
* B: Represents a measure related to the proportion of residents of African-American descent by town.<br> The variable is thought to reflect the extent of segregation in the area.
* LSTAT: Percentage of lower status of the population.
* MEDV: Median value of owner-occupied homes in $1000s (target variable).
## Significance of the Dataset
The Boston Housing dataset is not merely a collection of numbers but a catalyst that allows us to delve deeper into the realm of predictive analysis and regression modeling. Its comprehensiveness and diversity in features, from crime rates to nitrogen oxide concentration, enable practitioners to explore various angles of regression modeling, feature importance, and model interpretation. Moreover, the challenges it poses with multicollinearity among features, outliers, and leverage points introduce individuals to nuanced aspects of model tuning and validation.

This dataset stands as a testament to the potential of machine learning in deciphering patterns and making predictions in a real-world context. From simple linear regression models to advanced ensemble methods, the dataset provides a fertile ground for exploration, learning, and application of predictive modeling techniques in a meaningful context - predicting housing prices, an aspect integral to economic studies and policy-making.


