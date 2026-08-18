# Forecasting Children in HHS Care Using Machine Learning

## Project Overview

This project focuses on forecasting the number of children in HHS care using historical data and machine learning techniques.

The project uses Python and machine learning algorithms to analyze historical patterns and predict future values. Date-based features are extracted from the dataset and used to train regression models.

The main objective is to develop a forecasting system that can analyze historical HHS care data and provide predictions for future dates.

---

## Objectives

- Analyze historical HHS care data.
- Perform data preprocessing and cleaning.
- Extract useful date-based features.
- Visualize historical trends.
- Build machine learning regression models.
- Compare Linear Regression and Random Forest Regression.
- Evaluate model performance using MAE, RMSE, and R² score.
- Identify important features using Random Forest feature importance.
- Save the trained Random Forest model.
- Generate future predictions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook
- VS Code

---

## Machine Learning Models

Two regression models were developed and evaluated:

### 1. Linear Regression

Linear Regression was used as a baseline machine learning model.

### 2. Random Forest Regression

Random Forest Regression was used as the main machine learning model because it can capture nonlinear relationships between features and the target variable.

---

## Features Used

The following date-based features were used:

- year
- month
- day
- dayofweek
- dayofyear

### Target Variable

The target variable is:

`Children in HHS Care`

---

## Model Performance

The Random Forest model produced the following results on the test dataset:

| Metric | Result |
|---|---:|
| MAE | 182.40 |
| RMSE | 220.65 |
| R² Score | -0.5751 |

The Random Forest model performed better than the Linear Regression baseline according to the evaluated metrics, although the negative R² score indicates that the current model does not explain the test-set variation sufficiently well.

---

## Feature Importance

The Random Forest model identified the following feature importance values:

| Feature | Importance |
|---|---:|
| year | 0.682628 |
| dayofyear | 0.279483 |
| month | 0.033299 |
| day | 0.004078 |
| dayofweek | 0.000512 |

The `year` feature was the most influential feature, followed by `dayofyear`.

---

## Project Workflow

The project follows these major steps:

1. Load the dataset.
2. Inspect the dataset.
3. Clean and preprocess the data.
4. Convert the date column into datetime format.
5. Perform exploratory data analysis.
6. Extract date-based features.
7. Split the data into training and testing datasets.
8. Train Linear Regression.
9. Train Random Forest Regression.
10. Evaluate the models.
11. Analyze feature importance.
12. Generate actual vs predicted visualizations.
13. Save the trained Random Forest model.
14. Generate future predictions.
15. Document the results and conclusion.

---

## Results Visualization

The project includes visualizations for:

- Historical HHS care trends
- Actual vs Predicted values
- Random Forest feature importance

---

## Model File

The trained Random Forest model is stored in:

`model/random_forest_hhs_care_model.pkl`

The model can be loaded using Joblib and reused for prediction.

---

## Limitations

The current model has a negative R² score, which indicates that the model needs further improvement for reliable forecasting.

The current model uses mainly date-based features. It does not include other factors that may influence the number of children in HHS care.

Random Forest also does not naturally extrapolate beyond the range of years present in the training data.

---

## Future Improvements

Future versions of this project can include:

- Additional relevant features.
- More historical data.
- Lag features.
- Rolling averages.
- Hyperparameter tuning.
- Time-series forecasting models.
- Cross-validation designed for time-series data.
- Additional machine learning algorithms.
- Better feature engineering.
- Improved forecasting evaluation.

---

## Conclusion

This project demonstrates the use of Python and machine learning for analyzing and forecasting the number of children in HHS care.

The workflow includes data preprocessing, exploratory analysis, feature engineering, model development, model evaluation, feature importance analysis, and future prediction.

Random Forest Regression was used as the main model and achieved an MAE of approximately 182.40, an RMSE of approximately 220.65, and an R² score of approximately -0.5751 on the test dataset.

Feature importance analysis showed that year was the most influential feature, followed by dayofyear.

Although the current model requires further improvement for reliable forecasting, the project provides a complete machine learning workflow and establishes a foundation for developing a more accurate forecasting system.