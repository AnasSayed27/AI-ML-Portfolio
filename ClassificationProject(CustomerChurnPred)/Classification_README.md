# **Telco Customer Churn Prediction**

This project focuses on building a classification model to predict customer churn for a telecommunications company. Identifying customers who are likely to churn is a critical business need, as it allows the company to take proactive steps to retain them.

## **Problem Statement**

To develop a machine learning model that can accurately predict which customers are at a high risk of churning, based on their demographic data, account information, and the services they subscribe to.

## **Dataset**

The dataset used is the "Telco Customer Churn" dataset from Kaggle. It contains various features for 7043 customers.  
Link to Dataset

## **Tech Stack**

* Python  
* Pandas & NumPy  
* Matplotlib & Seaborn  
* Scikit-learn  
* XGBoost

## **Key Findings & Model Performance**

* **EDA Insights:** Analysis showed that customers with month-to-month contracts, fiber optic internet, and shorter tenures are more likely to churn.  
* **Data Preprocessing:** Handled missing values, encoded categorical features using both Label and One-Hot Encoding, and scaled numerical features.  
* **Model Comparison:** Three models were evaluated:  
  * **Logistic Regression:** Accuracy \= 81%, **Recall (for Churn) \= 0.57**  
  * **Random Forest:** Accuracy \= 79%, Recall (for Churn) \= 0.51  
  * **XGBoost:** Accuracy \= 79%, Recall (for Churn) \= 0.51

While all models had similar accuracy, the Logistic Regression model had the highest **recall** for the churn class. In a churn prediction scenario, maximizing recall is crucial to identify as many potential churners as possible.