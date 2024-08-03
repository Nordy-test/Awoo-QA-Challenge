import requests
from jsonpath_ng import parse


def 取得Json元素(json_string, expr, index=None):
    jsonpath_expr = parse(expr)
    elements = [match.value for match in jsonpath_expr.find(json_string)]
    return_data = elements if index is None else elements[index]
    return return_data


def Get_ID_Pokemon_Name(id):
    session = requests.Session()
    resp = session.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    json_data = resp.json()
    name_ls = 取得Json元素(json_data, '$.name')
    name = name_ls[0] if name_ls else None
    return name


if __name__ == "__main__":
    id = input("Enter Pokemon ID: ")
    pokemon_name = Get_ID_Pokemon_Name(id)
    print(pokemon_name)
