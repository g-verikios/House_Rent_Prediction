# %% IMPORTS
import pickle

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

# %% LOAD MODEL
model_file = 'model.bin'

with open(model_file, 'rb') as f_in: # now we read the file, its important to avoid to overwrite the file creating one with zero bytes

    (model) = pickle.load(f_in)


# %% PREDICT FUNCTION & APP
app = Flask('rent_pred') # create a flask app

@app.route('/predict', methods = ['POST']) 
 
def predict():

    listing = request.get_json()
    ### This should be inside a separate function ideally 
    # only the label encoder was used so we dont need the dict vectorizer for one-hot-encoding here 
    # we assume that the data coming in is preprocessed based on the EDA insights 
    X = np.array(list(listing.values()))
    X = X.reshape(1, -1)

    y_pred = model.predict(X)

    #### Need to convert the prediction since we used log1p
    result = {
        'Predicted Rent': float(np.expm1(y_pred))
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host ='localhost', port=9696) 