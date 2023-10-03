from flask import Flask, render_template_string, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Define a function to create a plot based on a DataFrame
def create_plot(df):
    plt.figure()
    df.plot(x='x', y='y')

    # Saving the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Convert the BytesIO object to base64 string
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return img_base64

@app.route('/')
def index():
    # Define the path to the data_files directory
    data_dir = '/home/srao/Documents/GitHub/PlotSat/plotsat/data_files/'

    filename = request.args.get('filename', 'file1.csv')
    csv_file_path = os.path.join(data_dir, filename)
    
    if not os.path.exists(csv_file_path):
        return "CSV file not found", 404

    df = pd.read_csv(csv_file_path)

    img_base64 = create_plot(df)
    
    # Create a simple template to display the plot and the message
    template = '''
    <h2>Hello, this is Flask!</h2>
    <img src="data:image/png;base64, {{ img_base64 }}">
    '''
    
    return render_template_string(template, img_base64=img_base64)

if __name__ == '__main__':
    app.run(port=5002, debug=True)

