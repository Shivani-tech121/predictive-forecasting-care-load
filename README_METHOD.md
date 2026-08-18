# Methodology and Technical Details

## 1. Data Collection

Historical data containing the number of children in HHS care was used for this project.

The dataset contains a date column and the corresponding number of children in HHS care.

---

## 2. Data Preprocessing

The dataset was loaded using Pandas.

The date column was converted into datetime format to allow extraction of useful temporal information.

The data was inspected for missing values, incorrect data types, and structural issues before model development.

---

## 3. Feature Engineering

The original date variable was transformed into several numerical features.

The following features were extracted:

- `year`
- `month`
- `day`
- `dayofweek`
- `dayofyear`

These features allow machine learning models to identify patterns associated with different periods of time.

The target variable was:

`Children in HHS Care`

---

## 4. Train-Test Split

The dataset was divided into training and testing datasets.

The training dataset contained:

- 576 samples

The testing dataset contained:

- 144 samples

Therefore:

- Training data = 80%
- Testing data = 20%

---

## 5. Linear Regression

Linear Regression was implemented as a baseline model.

The model attempts to establish a linear relationship between the date-based features and the number of children in HHS care.

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 6. Random Forest Regression

Random Forest Regression was implemented as the main machine learning model.

The model was configured using:

- Number of estimators = 200
- Random state = 42

The Random Forest model combines multiple decision trees to produce a regression prediction.

---

## 7. Random Forest Evaluation

The Random Forest model achieved the following test results:

### Mean Absolute Error

MAE = 182.4042

### Root Mean Squared Error

RMSE = 220.6510

### R² Score

R² = -0.5751

The negative R² score indicates that the current model does not capture the variation in the test dataset sufficiently well.

Therefore, the model should be considered a baseline forecasting model rather than a highly accurate production forecasting system.

---

## 8. Actual vs Predicted Analysis

An Actual vs Predicted plot was created to compare the actual number of children in HHS care with the values predicted by the Random Forest model.

The plot shows that the predicted values remain relatively close to a narrow range, while the actual values show substantially larger variation.

This difference helps explain the relatively poor R² score.

---

## 9. Feature Importance

Random Forest feature importance was calculated to identify which features contributed most to the model's predictions.

The results were:

| Feature | Importance |
|---|---:|
| year | 0.682628 |
| dayofyear | 0.279483 |
| month | 0.033299 |
| day | 0.004078 |
| dayofweek | 0.000512 |

The `year` feature had the highest importance at approximately 68.26%.

The `dayofyear` feature was the second most important feature at approximately 27.95%.

---

## 10. Model Saving

The trained Random Forest model is saved using Joblib.

The saved model file is:

`random_forest_hhs_care_model.pkl`

The model can later be loaded without retraining.

---

## 11. Future Prediction

The trained Random Forest model can be used to generate predictions for future dates.

Date-based features are first created for the future dates and then passed to the trained model.

The prediction output contains:

- Future date
- Predicted number of children in HHS care

---

## 12. Limitations

The current model has several limitations.

The most important limitation is the negative R² score. This indicates that the model does not explain the test-set variation sufficiently well.

The model currently relies primarily on date-based features. Other factors that may influence HHS care numbers are not included.

Another limitation is that Random Forest is not designed to extrapolate smoothly beyond the range of values seen during training.

---

## 13. Future Improvements

The forecasting performance can potentially be improved by adding:

- Lag features
- Rolling mean features
- Previous-day values
- Previous-week values
- Previous-month values
- Seasonal features
- More historical observations
- Hyperparameter optimization
- Time-series cross-validation
- Gradient Boosting models
- XGBoost
- Random Forest tuning
- Dedicated time-series forecasting models

---

# Final Conclusion

This project demonstrates an end-to-end machine learning workflow for forecasting the number of children in HHS care.

The workflow includes data preprocessing, feature engineering, exploratory analysis, train-test splitting, Linear Regression, Random Forest Regression, model evaluation, feature importance analysis, visualization, model saving, and future prediction.

The Random Forest model achieved an MAE of 182.40, an RMSE of 220.65, and an R² score of -0.5751.

Feature importance analysis showed that year was the most influential feature, followed by dayofyear.

The current results indicate that additional feature engineering and more suitable forecasting techniques are required to obtain a reliable forecasting model.