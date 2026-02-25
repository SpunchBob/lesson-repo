def print_list(list_: list) -> None:
    for val in list_:
        print(val)

def convert_dict_to_json_str(dict_: dict) -> str:
    result = "{\n"
    for key, value in dict_.items():
        result += f"    {key} : {value}\n"
    result += '}'
    return result 

if __name__ == "__main__":
    list_of_smth = [i for i in range(0, 10, 1)]
    dict_of_smth = {
        "addr" : "127.0.0.1",
        "host" : "8080",
        "route" : "/dev/api/images/get_image",
    }
    print(convert_dict_to_json_str(dict_of_smth))
    print_list(list_of_smth)
