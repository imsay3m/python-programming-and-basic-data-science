# Adult Income Prediction Project

## Project Overview

This project aims to predict whether an individual's income is above or below $50,000 based on various demographic and socioeconomic factors. The project utilizes the Adult dataset, a publicly available dataset from the UCI Machine Learning Repository.

## Dataset

The Adult dataset contains information about individuals, including their age, workclass, education, marital status, occupation, race, sex, capital gain, capital loss, hours per week worked, and native country. The target variable is 'income', which is binary and indicates whether the individual's income is above or below $50,000.

## Data Preprocessing

The following data preprocessing steps were performed:

1. **Handling Missing Values:** Missing values, represented by '?', were replaced with NaN. Rows with missing values in critical columns were dropped.
2. **Feature Selection:** Irrelevant or redundant features, such as 'fnlwgt', 'education', and 'native-country', were removed.
3. **Feature Engineering:** Categorical features, such as 'workclass', 'marital-status', 'occupation', 'race', and 'sex', were converted into numerical representations
4. **Data Splitting:** The dataset was split into training and testing sets using an 80/20 ratio.

## Model Selection and Training

Logistic Regression was chosen as the classification model due to its simplicity and effectiveness for binary classification problems. The model was trained using the training dataset.

## Prediction and Evaluation

The trained model was used to predict the income of individuals in the testing dataset. The model's performance was evaluated using the accuracy metric.

## Results

The Logistic Regression model achieved an reasonable accuracy on the testing dataset. This indicates that the model is able to predict income with a reasonable level of accuracy.

## Conclusion

This project demonstrates the application of machine learning techniques to predict income based on demographic and socioeconomic factors. The results show that Logistic Regression is a suitable model for this task. Further improvements could be explored by using different models, feature engineering techniques, or hyperparameter tuning.

## Code

The code for this project is available in the accompanying Jupyter Notebook. The notebook includes detailed explanations of each step in the process.

## References

- Adult dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult)
