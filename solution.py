import requests # import requests library for use

api_result = requests.get('https://api.aviationstack.com/v1/flights?access_key=2c60a151dd8c99eb71b9547bfeaac43a') # requests the data from the endpoint
# to add other parameters you can add "&parameter=value&parameter2=value2" etc.

# Or you can do it this way
# payload = {
    # "access_key" : "2c60a151dd8c99eb71b9547bfeaac43a"
# }
# api_result = requests.get('https://api.aviationstack.com/v1/flights', params=payload)

print(api_result.status_code) # code determining if the request was ok

api_result = api_result.json() # converts json to dicitonary
data = api_result["data"] # grabs only the "data" element from the response

for flight in data: # loops through all flights 
    if (flight["flight_status"] == "active"): # checks if flight is active 
        print("Flight airline: " + flight["airline"]["name"]) # airline
        print("Flight date: " + flight["flight_date"]) # date of flight
        print("Flight departure airport: " + flight["departure"]["airport"]) # departure airport
        print("Flight arrival airport: " + flight["arrival"]["airport"]) # arrival airport
        print("-----------------------------------------------")