from flask import Flask, render_template, request
import joblib
import sklearn
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

#models loads
model = joblib.load('model_gb.joblib')
model_nn = joblib.load('model_nn.joblib')

#importing dataset for the second model
data = pd.read_csv('data_model_2_clean.csv')

#home page
@app.route('/')
def home():
    return render_template('index_home.html')


#page of laptop price prediction model
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    val_predict = None
    y_pred = None
    if request.method == 'POST':
        ram = int(request.form['ram'])
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        cpu = float(request.form['cpu'])
        screen_size = float(request.form['ss'])
        os = int(request.form['os'])
        gpu = int(request.form['gpu'])
        condition = int(request.form['condition'])

        laptop = np.array([[hdd+ssd, hdd, ssd, screen_size, ram, cpu, os, gpu, condition]])

        y_pred = model.predict(laptop)

    return render_template('index_predict.html', val_predict=y_pred)

#page of laptop suggestion model
@app.route('/suggest', methods=['GET','POST'])
def suggest():
    laptops = None
    user_price = None
    if request.method == 'POST':
        user_price = float(request.form['price'])
        price_input = [[user_price]]
        distances, indices = model_nn.kneighbors(price_input)
        laptops = data.iloc[indices[0]].to_dict(orient='records')

    return render_template('index_suggest.html',laptops=laptops) 


if __name__=='__main__':
    app.run(debug=True)