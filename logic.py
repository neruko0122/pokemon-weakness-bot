import file_import
import constants
from linebot.models import (
    QuickReplyButton, MessageAction
)


pokemon_data = file_import.import_pokemon_data()
weakness_list = constants.WEAKNESS_LIST
types = constants.TYPES
normal_skills = constants.NORMAL_SKILLS
special_skills = constants.SPECIAL_SKILLS


def find_pokemon(message):
    for target in types:
        if target[0] == message:
            return set_reply_message(get_weakness(target))
    for normal in normal_skills:
        if normal['name'] == message:
            return set_reply_skill_message(normal)
    for special in special_skills:
        if special['name'] == message:
            return set_reply_skill_message(special)
    for pokemon in pokemon_data:
        if pokemon['name'] == message:
            return set_reply_message(get_weakness(pokemon['types']))
    print('not found pokemon')
    return constants.POKEMON_NOT_FOUND_MESSAGE


def find_suggest(message):
    suggest_list = []
    for pokemon in pokemon_data:
        if message in pokemon['name']:
            suggest_list.append(pokemon['name'])
    return suggest_list


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
        reply_message += '[' + types[0] + '/' + types[1] + ']タイプで、'
    else:
        reply_message += '[' + types[0] + ']タイプで、'

    if len(weakness['double']) > 0:
        reply_message += '\n◎2重弱点(x2.56)：'
        for double in weakness['double']:
            reply_message += '[' + double + ']'

    if len(weakness['single']) > 0:
        reply_message += '\n○弱点(x1.6)：'
        for single in weakness['single']:
            reply_message += '[' + single + ']'

    if len(strength['double']) > 0:
        reply_message += '\n▲2重耐性(x0.39)：'
        for double in strength['double']:
            reply_message += '[' + double + ']'

    if len(strength['single']) > 0:
        reply_message += '\n△耐性(x0.625)：'
        for single in strength['single']:
            reply_message += '[' + single + ']'

    if len(strength['noEffect']) > 0:
        reply_message += '\n×強耐性(x0.244)：'
        for noEffect in strength['noEffect']:
            reply_message += '[' + noEffect + ']'

    return reply_message


def set_reply_skill_message(skill):
    name = skill['name']
    category = skill['category']
    reply_message = ''

    if category == 'ノーマル':
        reply_message += '【' + name + '】は「' + skill['type'] + '」タイプで、'
        reply_message += '1ターンあたりのダメージ量は' + skill['dpt'] + '、'
        reply_message += '1ターンにためられるエネルギー量は' + skill['ept'] + 'です'
    else:
        reply_message += '【' + name + '】は「' + skill['type'] + '」タイプで、'
        reply_message += '1エネルギーあたりのダメージ量は' + skill['dpe'] + '、'
        reply_message += '消費エネルギー量は' + skill['energy'] + 'です'
        if skill['effect'] != '-':
            reply_message += 'また、特殊効果は' + skill['effect'] + 'です'

    return reply_message


def get_quick_reply(suggest_list):
    quick_reply_list = []
    for suggest in suggest_list:
        quick_reply_list.append(QuickReplyButton(action=MessageAction(label=suggest, text=suggest)))
    return quick_reply_list
