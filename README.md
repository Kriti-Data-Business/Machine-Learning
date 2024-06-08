# Machine-Learning

# Cross Validation in Machine Learning

## Overview

Cross-validation is a vital technique in machine learning used to evaluate the performance and generalizability of models. This repository provides an in-depth look at cross-validation, including its purpose, when to use it, and various types with examples and syntax.

## Table of Contents

1. [What is Cross-Validation?](#what-is-cross-validation)
2. [When is Cross-Validation Used?](#when-is-cross-validation-used)
3. [Types of Cross-Validation](#types-of-cross-validation)

## What is Cross-Validation?

Cross-validation is a statistical method used to estimate the skill of machine learning models. It involves splitting the dataset into a set of training and testing sets multiple times in different ways, training the model on the training sets, and evaluating it on the testing sets. This helps in assessing how well the model will perform on an independent dataset.

## When is Cross-Validation Used?

Cross-validation is used to:
- Estimate the performance of a model on unseen data.
- Prevent overfitting by ensuring the model performs well on multiple splits of the data.
- Compare the performance of different machine learning algorithms or models.
- Tune hyperparameters by providing a reliable performance metric.

## Types of Cross-Validation

Cross-validation can be performed in several ways. The main types include:

1. [K-Fold Cross-Validation](#k-fold-cross-validation)
2. [Stratified K-Fold Cross-Validation](#stratified-k-fold-cross-validation)
3. [Leave-One-Out Cross-Validation (LOOCV)](#leave-one-out-cross-validation-loocv)
4. [Repeated K-Fold Cross-Validation](#repeated-k-fold-cross-validation)
5. [Time Series Cross-Validation (Rolling Forecast Origin)](#time-series-cross-validation-rolling-forecast-origin)

## Folders for Each Type of Cross-Validation

Each type of cross-validation has its own folder in this repository, containing explanations, examples, and syntax. Below are the details:

### K-Fold Cross-Validation

- **Explanation**: Standard method where the dataset is divided into \( k \) equal-sized folds. The model is trained \( k \) times, each time using a different fold as the test set and the remaining \( k-1 \) folds as the training set.
- **Example and Syntax**: [Link to Folder](./K-Fold-Cross-Validation)

### Stratified K-Fold Cross-Validation

- **Explanation**: Similar to K-Fold but ensures each fold maintains the same class distribution as the entire dataset. Useful for imbalanced datasets.
- **Example and Syntax**: [Link to Folder](./Stratified-K-Fold-Cross-Validation)

### Leave-One-Out Cross-Validation (LOOCV)

- **Explanation**: Each sample in the dataset is used once as the test set while the remaining samples form the training set. This process is repeated for each sample.
- **Example and Syntax**: [Link to Folder](./Leave-One-Out-Cross-Validation)

### Repeated K-Fold Cross-Validation

- **Explanation**: Repeats the K-Fold process multiple times with different random splits of the data to provide a more robust performance estimate.
- **Example and Syntax**: [Link to Folder](./Repeated-K-Fold-Cross-Validation)

### Time Series Cross-Validation (Rolling Forecast Origin)

- **Explanation**: Used for time series data, this method respects the temporal order by training on increasing time spans and testing on the next time step.
- **Example and Syntax**: [Link to Folder](./Time-Series-Cross-Validation)

---

Each folder contains:

- **Detailed Explanation**: A deeper dive into the method and its applications.
- **Example**: A practical example using a sample dataset.
- **Syntax**: Python code implementing the cross-validation technique using scikit-learn.

Explore the folders to learn more about each cross-validation technique and see them in action with real code examples.

---

By following this structure, users can easily navigate through different cross-validation methods and understand their applications with practical examples and clear explanations.
