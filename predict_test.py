import requests

url = "http://localhost:9696/predict"


# %%
response = requests.post(url, json = prospect).json()

print(response)