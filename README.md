Overview

The Laptop Price Prediction and eBay Laptop Suggestions project is a data-driven solution designed to assist users in estimating laptop prices and discovering similar products available on eBay.
This project integrates machine learning and web development to solve two key challenges in the e-commerce laptop market:

1 . Laptop Price Prediction — Predicting laptop prices based on their technical specifications such as brand, processor speed, RAM, storage type, GPU, screen size, and operating system.

Several regression models were implemented and compared, including:
Linear Regression
Random Forest Regression
Gradient Boosting Regression
AdaBoost Regression
XGBoost Regression
Among these, the Gradient Boosting Regressor achieved the best results with an R² score of 0.81, demonstrating high predictive accuracy.

2 . Laptop Suggestions System — Recommending laptops that are most similar in price to a user-defined budget using the Nearest Neighbors algorithm.

Data for these recommendations was scraped from eBay using BeautifulSoup and Requests.
The system returns five similar laptops including images, titles, prices, and direct eBay links.
The application features a web interface built with HTML, CSS, and Flask, offering an intuitive and interactive way for users to:
Input laptop specifications
Get a predicted price
View similar laptop suggestions directly from eBay

Technical Highlights

Data Collection: 7000+ eBay laptop listings scraped and preprocessed.
Data Cleaning & Encoding: Handled missing values, normalized prices, encoded categorical variables (Brand, GPU, CPU Brand, OS, Condition).
Model Evaluation Metrics: MAE, MSE, and R²-score.
Best Performing Model: Gradient Boosting Regressor (R² = 0.81).

Deployment: Flask-based web app for real-time price prediction and product recommendation.
predictive analytics and recommendation systems can enhance the online shopping experience through intelligent automation.
