import requests
from jsonpath_ng import parse


def 取得Json元素(json_data, expr, index=None):
    jsonpath_expr = parse(expr)
    elements = [match.value for match in jsonpath_expr.find(json_data)]
    return_data = elements if index is None else elements[index]
    return return_data


def Get_ID_Pokemon_Data(id):
    session = requests.Session()
    resp = session.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    json_data = resp.json()
    name_ls = 取得Json元素(json_data, '$.name')
    name = name_ls[0] if name_ls else None
    types_ls = 取得Json元素(json_data, '$.types[*].type.name')
    pokemon_dic = {'id': id, 'name': name, 'types': types_ls}
    return pokemon_dic


def List_Pokemon_Data_Sorted_By_ID():
    data_ls = []
    for index in range(1, 20):
        pokemon_data = Get_ID_Pokemon_Data(index)
        data_ls.append(pokemon_data)
    sorted_list = sorted(data_ls, key=lambda x: x['id'])
    return sorted_list


if __name__ == "__main__":
    sorted_pokemon_data = List_Pokemon_Data_Sorted_By_ID()
    for pokemon in sorted_pokemon_data:
        print(
            f"ID: {pokemon['id']}, Name: {pokemon['name']}, Types: {pokemon['types']}")
