 Cancer Gene Expression Classification Pipeline

 Overview

This project implements a modular machine learning pipeline for cancer subtype classification using gene expression data.

The goal is to simulate a simplified computational oncology workflow inspired by TCGA-based cancer classification studies.



 Objectives

- Load and preprocess gene expression datasets
- Train multiple machine learning models
- Compare model performance
- Identify important genes contributing to classification
- Build a reproducible computational biology pipeline



 Methodology

1. Data Processing
- Gene expression matrix (samples × genes)
- Cancer subtype labels
- Missing value handling
- Feature scaling using StandardScaler

2. Machine Learning Models
- Random Forest Classifier
- Logistic Regression

3. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

4. Biological Interpretation
- Feature importance used to identify key predictive genes

---

Pipeline Structure
