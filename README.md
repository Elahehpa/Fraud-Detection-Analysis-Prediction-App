# Fraud Detection Analysis & Prediction App

This project demonstrates an **end-to-end fraud detection pipeline** using Python, pandas, scikit-learn, and Streamlit. It includes **data exploration, preprocessing, model training, evaluation, and a web-based prediction app**.

---

## **Dataset**

- The dataset used: https://www.kaggle.com/code/kifayatullahe/fraud-detection-ml-100-accuracy  (`AIML Dataset.csv`)
- Contains transaction information including:
  - Transaction type (`type`)
  - Amounts (`amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`)
  - Fraud labels (`isFraud`, `isFlaggedFraud`)

---

## **Key Steps**

1. **Exploratory Data Analysis (EDA)**
   - Checked missing values, distributions, and correlations.
   - Visualized fraud patterns by transaction type, amount, and time steps.
   - Analyzed top senders and receivers for fraudulent transactions.

2. **Feature Engineering**
   - Created `balanceDiffOrig` and `balanceDiffDest`.
   - Dropped irrelevant columns like `nameOrig`, `nameDest`, `step`, `isFlaggedFraud`.

3. **Data Preprocessing**
   - Categorical features encoded using `OneHotEncoder`.
   - Numerical features scaled using `StandardScaler`.

4. **Model Training**
   - Used **Logistic Regression** with `class_weight='balanced'` to handle class imbalance.
   - Evaluated using classification report, confusion matrix, and accuracy score.
   - Pipeline saved with `joblib` for Streamlit app integration.

5. **Streamlit Web App**
   - Users can input transaction details.
   - Predicts whether a transaction is **fraudulent** or **legitimate**.
   - Provides interactive visualization of predictions.
 

---

## **How to Run**

1. Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib

streamlit run fraud_detection.py
<img width="468" height="645" alt="image" src="https://github.com/user-attachments/assets/adce95dd-a078-4c07-b87f-bb96b573d043" />
