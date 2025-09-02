# **Car Price Prediction**

This project aims to predict the selling price of used cars using various features like the car's age, kilometers driven, fuel type, and seller type.

## **Problem Statement**

To build a regression model that accurately estimates the value of a used car, which is valuable for both buyers and sellers in the second-hand car market.

## **Dataset**

The dataset used for this project is the "CAR DETAILS FROM CAR DEKHO" dataset, which is publicly available on Kaggle.  
Link to Dataset

## **Tech Stack**

* Python  
* Pandas  
* NumPy  
* Matplotlib & Seaborn (for visualization)  
* Scikit-learn (for model building and evaluation)

## **Key Findings & Model Performance**

* **Feature Engineering:** A new feature, car\_age, was created from the year column, which proved to be a strong predictor.  
* **EDA Insights:** Exploratory Data Analysis revealed a strong negative correlation between a car's age and its selling price.  
* **Model Comparison:** Two models were built and evaluated:  
  * **Linear Regression (Baseline):** R² Score \= 0.49  
  * **Random Forest Regressor:** R² Score \= 0.69

The Random Forest Regressor performed significantly better, indicating that it captured the non-linear relationships in the data more effectively.