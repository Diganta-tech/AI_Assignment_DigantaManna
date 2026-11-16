# Customer Support Ticket Classification System

## 1. Project Overview

The Customer Support Ticket Classification System is a machine learning-based application that automatically classifies customer support tickets into predefined categories based on their descriptions.

The system uses TF-IDF for text feature extraction and Logistic Regression for classification.

It also provides confidence scores for predictions and generates automatic suggested responses based on the predicted category.

## 2. Problem Statement

Customer support teams receive numerous tickets every day. Manually categorising these tickets can be time-consuming.

The objective of this project is to automate ticket categorisation so that customer issues can be organised more efficiently.

The system classifies tickets into five categories:

- Login Issue
- Application Error
- Account Update
- Performance
- Report

## 3. Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Data Visualization:** Matplotlib
- **Machine Learning:** Scikit-learn
- **Feature Extraction:** TF-IDF Vectorizer
- **Classification Algorithm:** Logistic Regression
- **Model Saving:** Joblib
- **Dataset Format:** CSV

## 4. Dataset Information

A synthetic customer support ticket dataset was created for this assignment.

**Dataset Details:**

- Total Records: 200
- Total Categories: 5
- File Format: CSV

**Dataset Fields:**

The dataset contains the following columns:

- **ticket_id:** Unique ticket identifier.
- **ticket_description:** Description of the customer's issue.
- **category:** Category assigned to the ticket.
- **priority:** Priority level of the ticket (High, Medium, or Low).
- **status:** Current status of the ticket (Open, Closed, or In Progress).

The dataset contains 40 records for each category.

## 5. Project Structure

```text
AI_Assignment_DigantaManna/
│
├── data/
│   ├── tickets.csv
│   └── cleaned_tickets.csv
│
├── src/
│   ├── preprocessing.py
│   ├── eda.py
│   ├── train.py
│   ├── predict.py
│   ├── responses.py
│   └── app.py
│
├── model/
│   └── ticket_classifier.pkl
│
├── screenshots/
│   ├── category_distribution.png
│   ├── priority_distribution.png
│   ├── confusion_matrix.png
│   └── prediction.png
│
├── requirements.txt
├── README.md
└── report.pdf
```

## 6. Installation and Required Dependencies

**Step 1: Clone the repository**

```bash
git clone https://github.com/Diganta-tech/AI_Assignment_DigantaManna.git
cd AI_Assignment_DigantaManna
```

**Step 3: Install the required dependencies**

```bash
pip install -r requirements.txt
```

## 7. Data Preprocessing

Run the preprocessing script to clean the dataset:

```bash
python src/preprocessing.py
```

The script performs:

- Missing value checking and handling.
- Duplicate record removal.
- Text lowercasing.
- Removal of unnecessary special characters and punctuation.
- Whitespace normalization.

The cleaned dataset is saved as `data/cleaned_tickets.csv`.

## 8. Exploratory Data Analysis

Run the EDA script:

```bash
python src/eda.py
```

The script analyses ticket categories, priorities, and statuses and generates visualizations.

The charts are saved in the `screenshots/` directory.

## 9. Model Training and Testing

Run the training script:

```bash
python src/train.py
```

The training process includes:

1. Loading the cleaned dataset.
2. Splitting the dataset into 80% training and 20% testing data.
3. Converting ticket descriptions into numerical features using TF-IDF.
4. Training the Logistic Regression classifier.
5. Evaluating the model using Accuracy, Precision, Recall, F1-score, and a Confusion Matrix.

The trained model is saved as:

```text
model/ticket_classifier.pkl
```

## 10. New Ticket Prediction

To predict the category of a new ticket, run:

```bash
python src/predict.py
```

The program provides two options:

1. Predict a new ticket.
2. Test five new ticket descriptions.

It displays the predicted category and confidence score.

## 11. Running the Application

Run the command-line application:

```bash
python src/app.py
```

The application accepts a ticket description and displays:

- Predicted category.
- Confidence score.
- Suggested automatic response.

The suggested response is generated using a rule-based approach according to the predicted category.

## 12. Sample Input and Output

**Sample Input:**

```text
I am unable to login because my password is not working.
```

**Sample Output:**

```text
=============================================
       CUSTOMER SUPPORT CLASSIFIER
=============================================

Enter Ticket Description: I am unable to login because my password is not working.

---------------------------------------------
Predicted Category: Login Issue
Confidence: [Model-generated score]%

Suggested Response:
Please use the 'Forgot Password' option
on the login page to reset your password.
If the problem continues, please contact
the support team.
---------------------------------------------
```

The confidence score depends on the model's prediction.