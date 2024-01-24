import requests

url = "http://localhost:9696/predict"

listing_id = '0115jbjfe' # random listing id that hypothetically corresponds to a house listing with the below characteristics

# Here we assume the request is made after the data has been properly processed based on the isights from the EDA so I use the final form of the data
listing = {'posted_on': 174,
'bhk': 2,
'size': 1100,
'floor': 247,
'area_type': 2,
'area_locality': 875,
'city': 0,
'furnishing_status': 2,
'tenant_preferred': 1,
'bathroom': 2,
'point_of_contact': 2
}
# %%
response = requests.post(url, json = listing).json()

print(response)

print(f"Rent for listing {listing_id} is {response['Predicted Rent']}")