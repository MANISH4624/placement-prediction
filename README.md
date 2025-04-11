Placement Prediction Project
Overview
This project focuses on predicting student placement status based on various academic and demographic factors. The dataset includes features such as academic percentages, work experience, specialization, and more. The goal is to build a model that can accurately classify whether a student will be placed or not.

Dataset
The dataset contains the following features:

sl_no: Serial Number

gender: Gender of the student (M/F)

ssc_p: Secondary Education percentage (10th Grade)

hsc_p: Higher Secondary Education percentage (12th Grade)

hsc_s: Specialization in Higher Secondary Education (Commerce, Science, Arts)

degree_p: Degree Percentage

degree_t: Under Graduation Degree type (Sci&Tech, Comm&Mgmt, Others)

workex: Work Experience (Yes/No)

etest_p: Employability test percentage (conducted by college)

specialisation: Post Graduation (MBA) Specialization (Mkt&HR, Mkt&Fin)

mba_p: MBA percentage

status: Status of placement (Placed/Not Placed)

Data Preprocessing
Handling Missing Values: The dataset was checked for null values, and missing values in the salary column were filled with 0.

Outlier Removal: Outliers in numerical columns (ssc_p, hsc_p, degree_p, etest_p, mba_p) were removed using the IQR method.

Feature Encoding:

Binary categorical columns (gender, workex, status) were label encoded.

Other categorical columns (hsc_s, degree_t, specialisation) were one-hot encoded.

Feature Scaling: Numerical columns were standardized using StandardScaler.

Model Building
A Logistic Regression model was trained to predict the placement status. The dataset was split into training (80%) and testing (20%) sets.

Model Performance
Accuracy: 85.71%

Classification Report:

Precision: 0.88 (Placed), 0.78 (Not Placed)

Recall: 0.94 (Placed), 0.64 (Not Placed)

F1-Score: 0.91 (Placed), 0.70 (Not Placed)

How to Use
Install Dependencies: Ensure you have Python and the required libraries (NumPy, Pandas, scikit-learn) installed.

Load the Model: The trained Logistic Regression model is saved as placement_model.pkl and can be loaded using the pickle module.

Make Predictions: Use the model to predict placement status by passing preprocessed input data.

Future Improvements
Experiment with other classification algorithms (e.g., Random Forest, SVM).

Perform hyperparameter tuning to improve model performance.

Include additional features or external data sources for better predictions.

Project Structure
placementNEW.ipynb: Jupyter notebook containing the data analysis, preprocessing, and model training.

placement_model.pkl: Serialized Logistic Regression model for deployment.

Placement_Data.csv: Original dataset used for training 
