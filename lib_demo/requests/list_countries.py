import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
# print(resp.text)

for c in resp.json():
    print("%-50s %s" % (c["name"], c["capital"]))
