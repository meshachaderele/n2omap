from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dummy N2O data
n2o_data_df = pd.read_csv("n2o_emission_data.csv")

@app.route('/')
def index():
    # This renders the `index.html` file from the `templates` folder
    return render_template('index.html')

@app.route('/n2o_data/<region>')
def n2o_data(region):
    # Filter the N2O data for the selected region
    region_data = n2o_data_df[n2o_data_df['Region'] == region]
    
    # Check if region_data is empty (in case no matching region is found)
    if region_data.empty:
        return jsonify([])  # Return an empty list if no data for the region

    # Drop the Region column and transpose the DataFrame for yearly emissions
    year_data = region_data.drop(columns=["Region"]).T
    year_data.columns = ['Emission']
    year_data['Year'] = year_data.index
    return jsonify(year_data.to_dict('records'))

    print(region_data)


if __name__ == '__main__':
    app.run(debug=True)


