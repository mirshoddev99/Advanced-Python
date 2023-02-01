import requests
import pprint
import json

URL = "http://api.tvmaze.com/singlesearch/shows"
params = {"q":"jenny"}

res = requests.get(URL, params=params)

if res.status_code == 200:
    json = json.loads(res.text)
    # pprint.pprint(json)
    #
    # print("\nKeys {}".format(json.keys()))

    name = json["name"]
    premiered = json["premiered"]
    language = json["language"]
    country = json["network"]["country"]["name"]
    off_site = json["network"]["officialSite"]
    status = json["status"]
    print(
        f"""
            name: {name}
            premiered: {premiered}
            language: {language}
            country: {country}
            OfficialSite: {off_site}
            status: {status} 
        """
          )

else:
    print("An error occurred")
