import requests
import json


def get_homeworld_name(homeworld_url):
    homeworld_response = requests.request("GET", homeworld_url)
    homeworld_json = homeworld_response.json()
    return homeworld_json["name"]


def get_pilots_data(pilots_urls):
    result = []
    for pilot_url in pilots_urls:
        pilot_response = requests.request("GET", pilot_url)
        pilot_json = pilot_response.json()
        result.append({
            "name": pilot_json["name"],
            "height": pilot_json["height"],
            "mass": pilot_json["mass"],
            "homeworld_name": get_homeworld_name(pilot_json["homeworld"]),
            "homeworld": pilot_json["homeworld"],
        })
    return result


def get_starships_data(starships_url):
    ship_response = requests.request("GET", starships_url)
    ship_data = ship_response.json()
    result = []
    for ship_json in ship_data["results"]:
        result.append({
            "name": ship_json["name"],
            "max_atmosphering_speed": ship_json["max_atmosphering_speed"],
            "starship_class": ship_json["starship_class"],
            "pilots": get_pilots_data(ship_json["pilots"])
        })
    return result


URL = "https://swapi.dev/api/starships/?search=Millennium Falcon"
starships = get_starships_data(URL)

for starship in starships:
    filename = starship['name'] + '.json'
    with open(filename, "w") as json_file:
        json.dump(starships[0], json_file, indent=4)



