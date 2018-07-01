import requests

r = requests.get("http://srikanthtechnologies.com/rss.xml")
print(r)

if r.status_code == 200:
    print(r.text)
else:
    print("Sorry! URL not found!!")
