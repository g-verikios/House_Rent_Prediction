# %% IMPORTS
import pickle

from flask import Flask
from flask import request
from flask import jsonify

# %% LOAD MODEL
model_file = 'model.bin'

with open(model_file, 'rb') as f_in: # now we read the file, its important to avoid to overwrite the file creating one with zero bytes

    (dv, model) = pickle.load(f_in)


# %% PREDICT FUNCTION & APP

app = Flask('rent_pred') # create a flask app

@app.route('/predict', methods = ['POST']) 


def predict():
 

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host ='localhost', port=9696) 