# 🌸 K-Nearest Neighbors (KNN) Classification - Iris Dataset

## 📌 Objective
Implement and understand the **K-Nearest Neighbors (KNN)** algorithm for classification, test different values of `K`, and visualize decision boundaries.

## 📂 Dataset
- **Name**: Iris Dataset
- **Source**: Built-in dataset from `scikit-learn`
- **Description**: Contains 150 samples of iris flowers with 4 features (sepal length, sepal width, petal length, petal width) and 3 classes.

## 🛠 Tools & Libraries Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## 📋 Steps Performed
1. **Loaded the Dataset** using `load_iris()` from scikit-learn.
2. **Normalized Features** using `StandardScaler` (important for KNN).
3. **Split Data** into training (80%) and testing (20%) sets.
4. **Trained KNN Models** for K = 1 to 10 and recorded accuracy.
5. **Selected Best K** based on accuracy results.
6. **Evaluated Model** using accuracy score and confusion matrix.
7. **Visualized Decision Boundaries** using first 2 features.

## 📊 Results
- **Best K**: 5 (example from run)
- **Accuracy**: ~100% (varies slightly per run)
- **Confusion Matrix**: [[10 0 0]
                         [ 0 9 0]
                         [ 0 0 11]]
