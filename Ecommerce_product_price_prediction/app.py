from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and columns
model = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')  # Should be dumped during training

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/cloth')
def cloth():
    return render_template('cloth.html')
@app.route('/electronic')
def electronic():
    return render_template('electronic.html')
@app.route('/homedecor')
def homedecor():
    return render_template('homedecor.html')
@app.route('/beauty')
def beauty():
    return render_template('beauty.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        # Extract inputs
        user_input = {
            'original_price': float(data['original_price']),
            'discount_percentage': float(data['discount_percentage']),
            'rating': float(data['rating']),
            'review_count': int(data['review_count']),
            'seller_rating': float(data['seller_rating']),
            'competitor_price': float(data['competitor_price']),
            'demand_index': float(data['demand_index']),
            'shipping_cost': float(data['shipping_cost']),
            'category': data['category'],
            'brand': data['brand'],
            'stock_availability': data['stock_availability']
        }

        # Convert to DataFrame
        df = pd.DataFrame([user_input])

        # One-hot encode categorical features
        df = pd.get_dummies(df)

        # Add missing columns (set to 0)
        for col in model_columns:
            if col not in df.columns:
                df[col] = 0

        # Ensure column order matches model input
        df = df[model_columns]

        # Predict
        prediction = model.predict(df)[0]

        return jsonify({'price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
