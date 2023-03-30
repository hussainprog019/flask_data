from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['data_file']
    df = pd.read_csv(file)

    # perform data analysis
    num_rows, num_cols = df.shape
    missing_values = df.isna().sum()
    column_data_types = df.dtypes
    summary_stats = df.describe()

    return render_template('analysis.html', 
                       num_rows=num_rows, 
                       num_cols=num_cols, 
                       missing_values=missing_values, 
                       column_data_types=column_data_types, 
                       summary_stats=summary_stats)
    

if __name__ == '__main__':
    app.run(debug=True)
