import json


def import_pokemon_data():
    json_open = open('pokemon_data.json', 'r')
    data = json.load(json_open)

    return data
