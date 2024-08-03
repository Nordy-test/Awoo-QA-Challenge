import requests
from jsonpath_ng import parse


def 取得Json元素(json_data, expr):
    jsonpath_expr = parse(expr)
    elements = [match.value for match in jsonpath_expr.find(json_data)]
    return elements


def Get_ID_Pokemon_Data(id):
    session = requests.Session()
    resp = session.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    json_data = resp.json()
    name_ls = 取得Json元素(json_data, '$.name')
    name = name_ls[0] if name_ls else None
    weight_ls = 取得Json元素(json_data, '$.weight')
    weight = weight_ls[0] if weight_ls else None
    pokemon_dic = {'id': id, 'name': name, 'weight': weight}
    return pokemon_dic


def List_Pokemon_Data_Sorted_By_Weight():
    data_ls = []
    for index in range(1, 100):
        pokemon_data = Get_ID_Pokemon_Data(index)
        if pokemon_data['weight'] < 50:
            data_ls.append(pokemon_data)
    sorted_list = sorted(data_ls, key=lambda x: x['weight'], reverse=True)
    return sorted_list


if __name__ == "__main__":
    sorted_pokemon_data = List_Pokemon_Data_Sorted_By_Weight()
    for pokemon in sorted_pokemon_data:
        print(f"Name: {pokemon['name']}, Weight: {pokemon['weight']}")
