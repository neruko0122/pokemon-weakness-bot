import file_import
import constants


pokemon_data = file_import.import_pokemon_data()
weakness_list = constants.WEAKNESS_LIST


def find_pokemon(message):
    for pokemon in pokemon_data:
        if pokemon['name'] == message:
            print(pokemon['types'])
            print(len(pokemon['types']))
            print(get_weakness(pokemon['types']))
            return pokemon['types'][0]
    print('not found pokemon')
    return 'ポケモンの名前を正しく指定して下さい。'


def get_weakness(types):
    if len(types) >= 2:
        for weakness in weakness_list:
            if len(weakness['types'] < 2):
                continue
            else:
                if (types[0] == weakness['types'][0] and types[1] == weakness['types'][1]) or (types[0] == weakness['types'][1] and types[1] == weakness['types'][0]):
                    return weakness
            continue
    else:
        for weakness in weakness_list:
            if len(weakness['types'] > 1):
                continue
            else:
                if types[0] == weakness['types'][0]:
                    return weakness
            continue
