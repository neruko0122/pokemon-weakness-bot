import file_import


pokemon_data = file_import.import_pokemon_data()


def find_pokemon(message):
    for pokemon in pokemon_data:
        if pokemon['name'] == message:
            print(pokemon)
            return pokemon['types']
    print('not found pokemon')
    return 'ポケモンの名前を正しく指定して下さい。'
