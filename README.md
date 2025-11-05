# 💻 Laptop Price Prediction & eBay Suggestions

This project leverages machine learning to predict laptop prices based on technical specifications and suggests similar laptops from eBay listings based on a user's budget.

## 📌 Project Overview

The project is divided into two main components:

1. **Laptop Price Prediction**: Uses regression models to estimate laptop prices based on features like RAM, storage, CPU, GPU, screen size, etc.
2. **Laptop Suggestions**: Uses a Nearest Neighbors model to recommend 5 laptops from eBay that match a user's specified price.

## 📊 Dataset

- **Initial Data**: 7000 laptop listings scraped from eBay
- **Cleaned Data**: 358 rows × 12 columns
- **Features**: Brand, CPU Speed, CPU Brand, Storage Type, Storage (HDD/SSD), GPU, Screen Size, RAM, Condition, Operating System, Price

## 🧠 Machine Learning Models

### 🔹 Price Prediction Models

| Model                     | MAE (Test) | MSE (Test) | R² (Test) |
|---------------------------|------------|------------|-----------|
| Linear Regression         | 160.41     | 57995.87   | 0.39      |
| Decision Tree             | 119.32     | 37858.85   | 0.60      |
| Random Forest             | 95.92      | 26740.34   | 0.72      |
| **Gradient Boosting**     | **83.93**  | **17685.42**| **0.81**  |
| XGBoost                   | 102.12     | 2542.36    | 0.73      |
| AdaBoost                  | 150.79     | 30953.81   | 0.67      |

> ✅ **Best Model**: Gradient Boosting Regressor (after hyperparameter tuning with GridSearchCV)

### 🔹 Suggestion Model

- **Algorithm**: Nearest Neighbors
- **Purpose**: Recommend 5 laptops closest to the user's input price
- **Features Used**: Price, title, image, eBay link

## 🧩 Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, XGBoost, Pandas, NumPy
- **Web Scraping**: BeautifulSoup, Requests
- **Frontend**: HTML, CSS
- **Visualization**: Matplotlib, Seaborn

