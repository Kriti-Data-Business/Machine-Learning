
### 3. Leave-One-Out Cross-Validation (LOOCV)

#### Description
# - **Procedure**:
#   1. Each sample in the dataset is used once as the test set.
#   2. The remaining \( n-1 \) samples are used as the training set.
#   3. Repeat this process \( n \) times (where \( n \) is the number of samples).
#   4. Average the performance metrics over the \( n \) iterations.

# #### Example
# - **Usage**: When you have a very small dataset and want to make the most out of every data point.
# - **Example**: You have 10 samples. In each iteration, one sample is the test set and the remaining 9 samples are the training set.



from sklearn.model_selection import LeaveOneOut

# Define Leave-One-Out cross-validator
loocv = LeaveOneOut()

# Evaluate the model
loocv_scores = cross_val_score(model, X, y, cv=loocv)

print("Accuracy scores for each iteration: ", loocv_scores)
print("Mean accuracy: ", loocv_scores.mean())
