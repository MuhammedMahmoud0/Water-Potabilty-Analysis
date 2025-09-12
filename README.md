# 💧 Water Potability Analysis

## 📜 Overview
This project analyzes the quality of water to determine its potability (suitability for drinking) using machine learning models. It also includes a simple web application for users to interact with the results.

## 🚀 Features
- **Data Preprocessing**: Handled missing values, feature scaling, and feature engineering.
- **Machine Learning Models**:
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Naive Bayes
- **Model Evaluation**: Compared different models to identify the best-performing one.
- **Web Application**: Built with Flask and HTML/CSS for easy interaction.
- **Database Integration**: MongoDB used to store and retrieve model results and predictions.

## 🛠️ Technologies Used
- **Python** (Pandas, Scikit-learn, Matplotlib, Seaborn)
- **Flask** (for backend API and server)
- **MongoDB** (for database storage)
- **HTML & CSS** (for frontend interface)

## 📈 Machine Learning Workflow
1. Data Cleaning (Handling missing values using KNN Imputer)
2. Feature Engineering
3. Feature Scaling
4. Model Training & Testing
5. Model Evaluation using accuracy, precision, recall, and F1-score
6. Selection of Best Model
7. Deployment via Flask Web App

## 🖥️ Web Application Overview
- **Home Page**: Welcome page and project description.
- **Prediction Page**: Upload water quality features to predict potability.
- **Visualization Page**: Graphs and insights from the dataset.
- **Database Integration**: Results are stored/retrieved from MongoDB.z
