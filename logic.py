import file_import
import constants


pokemon_data = file_import.import_pokemon_data()
weakness_list = constants.WEAKNESS_LIST


def find_pokemon(message):
    for pokemon in pokemon_data:
        if pokemon['name'] == message:
            print(pokemon['types'])
            print(len(pokemon['types']))
            print(set_reply_message(get_weakness(pokemon['types'])))
            return set_reply_message(get_weakness(pokemon['types']))
    print('not found pokemon')
    return 'ポケモンの名前を正しく指定して下さい。'


def get_weakness(types):
    if len(types) >= 2:
        for weakness in weakness_list:
            if len(weakness['types']) < 2:
                continue
            else:
                if (types[0] == weakness['types'][0] and types[1] == weakness['types'][1]) or (types[0] == weakness['types'][1] and types[1] == weakness['types'][0]):
                    return weakness
            continue
    else:
        for weakness in weakness_list:
            if len(weakness['types']) > 1:
                continue
            else:
                if types[0] == weakness['types'][0]:
                    return weakness
            continue


def set_reply_message(effect):
    types = effect['types']
    weakness = effect['weakness']
    strength = effect['strength']
    reply_message = 'このポケモンは'

    if len(types) > 1:
        reply_message += '【' + types[0] + '】と【' + types[1] + '】タイプで、'
    else:
        reply_message += '【' + types[0] + '】タイプで、'

    if len(weakness['double']) > 1:
        reply_message += '2重弱点(x2.56)は、'
        for double in weakness['double']:
            reply_message += '【' + double + '】'
        reply_message += 'です。'

    if len(weakness['single']) > 1:
        reply_message += '弱点(x1.6)は、'
        for single in weakness['single']:
            reply_message += '【' + single + '】'
        reply_message += 'です。'

    if len(strength['double']) > 1:
        reply_message += '2重耐性(x0.39)は、'
        for double in weakness['double']:
            reply_message += '【' + double + '】'
        reply_message += 'です。'

    if len(strength['noEffect']) > 1:
        reply_message += '強耐性(x0.244)は、'
        for noEffect in weakness['noEffect']:
            reply_message += '【' + noEffect + '】'
        reply_message += 'です。'

    return reply_message

