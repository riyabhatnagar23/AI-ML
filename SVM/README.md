# SVM Classification - Breast Cancer Dataset

## 📌 Objective
Implement Support Vector Machines (SVM) with both **Linear** and **RBF** kernels for binary classification.

## 📂 Dataset
- **Name:** Breast Cancer Wisconsin Dataset
- **Source:** `sklearn.datasets.load_breast_cancer()`

## 🛠 Tools Used
- Python
- Scikit-learn
- NumPy
- Matplotlib

## 🚀 Steps Performed
1. Loaded and scaled the dataset.
2. Trained SVM with:
   - Linear Kernel
   - RBF Kernel
3. Tuned hyperparameters (`C` and `gamma`) using GridSearchCV.
4. Evaluated using Cross-validation.
5. Visualized decision boundary on first 2 features.

## 📊 Results
- **Linear Kernel Accuracy:** ~96%
- **RBF Kernel Accuracy:** ~98%
- **Best Params:** C=10, gamma=0.1



