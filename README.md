


# Heart Disease Prediction Using Logistic Regression

This repository contains a Python project for predicting the likelihood of heart disease using logistic regression. The project leverages a dataset from the Framingham Heart Study and demonstrates data preprocessing, exploratory data analysis, model training, and evaluation.

## Project Overview

Heart disease is a leading cause of death globally. Predicting the risk of developing heart disease can help in early diagnosis and preventive measures. This project uses logistic regression to model the relationship between risk factors and the likelihood of developing heart disease over a ten-year period.

## Dataset

The dataset used in this project is sourced from the Framingham Heart Study. It includes multiple risk factors for heart disease, such as:
- Age
- Gender
- Cigarettes smoked per day
- Total cholesterol
- Systolic blood pressure
- Glucose levels

## Features

- **Data Preprocessing**: 
  - Removal of irrelevant features like education.
  - Handling of missing values.
  - Normalization of feature data.

- **Exploratory Data Analysis (EDA)**:
  - Distribution of target variable (`TenYearCHD`).
  - Visualizations using Matplotlib and Seaborn.

- **Model Training**:
  - Logistic regression model trained on the processed dataset.

- **Model Evaluation**:
  - Accuracy score.
  - Confusion matrix with a heatmap.
  - Classification report.

## Prerequisites

The following libraries are required to run the code:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `statsmodels`

Install the libraries using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Siddharth261229/heart-disease-prediction.git
    cd heart-disease-prediction
    ```

2. Place the dataset file (`framingham.csv`) in the project directory.

3. Run the Python script:
    ```bash
    python heart_disease_prediction.py
    ```

## Results

- **Accuracy**: The logistic regression model achieves an accuracy of approximately X% on the test set.
- **Confusion Matrix**: The confusion matrix provides insights into true positives, false positives, true negatives, and false negatives.
- **Classification Report**: Detailed precision, recall, F1-score, and support metrics for each class.

## Visualizations

- Bar plot showing the distribution of `TenYearCHD`.
- Heatmap of the confusion matrix.

## Project Directory

```
heart-disease-prediction/
│
├── framingham.csv              # Dataset file
├── heart_disease_prediction.py # Main Python script
├── README.md                   # Project README file
└── requirements.txt            # Required Python libraries
```

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the project.



## Acknowledgments

- The dataset used is part of the Framingham Heart Study.
- Inspiration for this project came from the importance of early heart disease detection.

