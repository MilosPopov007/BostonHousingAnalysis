# Boston Housing Prices Prediction
## Introduction
The aim of my project is to predict the median value of owner-occupied homes in $1000s in various Boston suburbs. I used the famous Boston Housing dataset from the UCI Machine Learning Repository. This dataset consists of 506 entries with 14 attributes, where each entry represents data about a suburb of Boston.

## Data Preprocessing
### Missing Values
I found the dataset to be clean without any missing values, so no imputation was required.

### Feature Scaling
The features had different scales which could impact the performance of machine learning models. Therefore, I used the StandardScaler from sklearn to standardize the dataset, ensuring each feature has a mean of 0 and a standard deviation of 1.

### Feature Engineering
I didn't perform additional feature engineering, as the initial features provided sufficient information for the models.

## Model Building & Validation
I tested several algorithms on the dataset, including Linear Regression, Random Forest, and XGBoost. To find the best hyperparameters for the models, I employed grid search with cross-validation.

I used the Root Mean Squared Error (RMSE) as the evaluation metric since it provides a good indication of the model's prediction error in terms of the target variable's unit.

The XGBoost algorithm, after hyperparameter tuning, provided the best performance with an RMSE of approximately 2.38 on the test data.

## Model Interpretability
Using SHAP values, I was able to interpret the model's predictions. The top features impacting the housing prices were LSTAT (% lower status of the population), RM (average number of rooms per dwelling), and CRIM (per capita crime rate by town).

## Steps to Reproduce
Clone the repository.
Install the necessary libraries listed in requirements.txt.
Load the saved XGBoost model and scaler from the models directory.
Use the model to make predictions on new (scaled) data.
## Conclusion
This analysis provided valuable insights into the factors affecting housing prices in Boston suburbs. The XGBoost model was particularly effective in making predictions. Future work could explore deep learning techniques or more feature engineering for potentially improved performance.


