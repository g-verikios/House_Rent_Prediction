# House_Rent_Prediction
Predicting rent prices for a house dataset.


## House Rent Dataset
This dataset revovles around rent prices for houses in India. Since the housing market is at an all time high worldwide I had an interest in exploring such a dataset and work on regression. The description in kaggle is as follows:
'The spectrum of housing options in India is incredibly diverse, spanning from the opulent palaces once inhabited by maharajas of yore, to the contemporary high-rise apartment complexes in bustling metropolitan areas, and even to the humble abodes in remote villages, consisting of modest huts. This wide-ranging tapestry of residential choices reflects the significant expansion witnessed in India's housing sector, which has paralleled the upward trajectory of income levels in the country. According to the findings of the Human Rights Measurement Initiative, India currently achieves 60.9% of what is theoretically attainable, considering its current income levels, in ensuring the fundamental right to housing for its citizens. In the realm of housing arrangements, renting, known interchangeably as hiring or letting, constitutes an agreement wherein compensation is provided for the temporary utilization of a resource, service, or property owned by another party. Within this arrangement, a gross lease is one where the tenant is obligated to pay a fixed rental amount, and the landlord assumes responsibility for covering all ongoing property-related expenses. The concept of renting also aligns with the principles of the sharing economy, as it fosters the utilization of assets and resources among individuals or entities, promoting efficiency and access to housing solutions for a broad spectrum of individuals.'

The specifics of the features in this dataset can be found on the link in the references. The features as they appear in the `Dataset Glossary.txt` are:

| Feature           | Description                                                                               |
|-------------------|-------------------------------------------------------------------------------------------|
| BHK               | Number of Bedrooms, Hall, Kitchen.                                                        |
| Rent              | Rent of the Houses/Apartments/Flats.                                                      |
| Size              | Size of the Houses/Apartments/Flats in Square Feet.                                       |
| Floor             | Houses/Apartments/Flats situated in which Floor and Total Number of Floors (e.g., Ground out of 2, 3 out of 5, etc.) |
| Area Type         | Size of the Houses/Apartments/Flats calculated on either Super Area or Carpet Area or Build Area. |
| Area Locality     | Locality of the Houses/Apartments/Flats.                                                  |
| City              | City where the Houses/Apartments/Flats are Located.                                       |
| Furnishing Status | Furnishing Status of the Houses/Apartments/Flats, either it is Furnished or Semi-Furnished or Unfurnished. |
| Tenant Preferred  | Type of Tenant Preferred by the Owner or Agent.                                           |
| Bathroom          | Number of Bathrooms.                                                                      |
| Point of Contact  | Whom should you contact for more information regarding the Houses/Apartments/Flats.      |


References:
- https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset?select=House_Rent_Dataset.csv

Note: Some models and methods are inspired from work in regression from a previous student in the course of machine-learning-zoomcamp and some of the code has been adapted and re-used, a relevant notebook can be found in the [repo](https://github.com/kwangyy/midterm-project)
## Environent setup
The environment used for development is based on the course of [machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp), in the context of which this project is conducted. A nice detailed guide can be found [here](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_5-flask_and_docker_for_deployment/readme.md).

For the bare minimums to run this code you will need:
- pipenv that is used for python package management, you can install it in your terminal with `pip install pipenv`
- To be able to utilize the environment you need to open up a terminal in this repo folder and type: `pipenv shell` to activate the virtual environment and install the dependencies described in the pipfiles.
- Docker set up for your system (if you do not have it already you can check the guide above for installing docker)
- A wsl distro if you are on windows (again you can find details in the above guide) or simply be on ubuntu. 
  
## Contents
- notebook.ipynb: the notebook where an exploratory data analysis (EDA) is conducted and the best performing model is selected
- Dockerfile: used to containerize the application
- Leads.csv: the dataset
- train.py: the script that trains the model based on the insights from the EDA in the notebook
- model.bin: the binary file that contains the trained model
- predict.py: the script used in the containerized application that creates a flask app for prediction using the model
- Pipfile & Pifile.lock: files used to set up the virtual environment for pipenv
- predict_test.py: script that tests the prediction app making a request to the prediction service. There are two example dictionaries that could be used (commenting one and uncommenting the other) to make the test requests.

## Exploratory Data Analysis
Insigths were found through an EDA on the dataset, in the notebook. Here I am be using the dataset to predict the target variable rent using the following models for regression:
- Linear Regression
- Ridge regression  (linear with regularization)
- Decision Tree regressor
- Random forest regressor
- XGBregressor 
These models are compared to choose the one with the best performance based on root mean squared error (RMSE).

## How to use
### Notebook with EDA
  After setting up the environment using pipenv you can open the notebook with: `jupyter notebook notebook.ipynb`
### Model training
  Simply open a terminal in this folder and type: `pipenv run python train.py`
### Running the service (local) and testing
1. Build the docker image using `docker build -t rent-prediction .`
2. Run the docker image and deploy the service locally using `docker run -it --rm -p 9696:9696 rent-prediction`
3. In a terminal with the pipenv environment activated type and run: `python predict_test.py`, this runs a test and should return the response from the service similar to the screenshot below.

This is what it should like:


Note: To stop serving use Crtl+C

## Things that could be done better and other remarks
- The part of handling the features, for e.g. which ones to drop which ones to keep could be set up perhaps in a better way so that it's customizable in a simpler way. Now the column names are hardcoded and this is probably not the cleanest option if a later EDA on newer datasets brings other insights in terms of feature importance etc.
- Generally wanted to do something more exotic other than the boilerplate used in the course for the scripts deploying the model, but in this case time was really limited, perhaps something to change in the future.
- Serving the app on a webserver instead of local deployment
- For serving the app on windows instead of ubuntu you could use waitress to serve the flask application, a few modifications might be needed in the Dockerfile and the pipfiles