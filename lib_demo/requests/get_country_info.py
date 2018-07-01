import requests

country_code = input("Enter country code: ")
resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + country_code)

if resp.status_code == 200:
    print(resp.json()["name"])
    print(resp.json()["capital"])
else:
    print('Sorry! Country not found!!')
