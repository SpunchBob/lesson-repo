def print_list(list_: list) -> None:
    for val in list_:
        print(val)

def generator_inertation(start: int, end: int) -> list:
    list_ = [i for i in range(start, end, 1)]
    return list_

def convert_dict_to_json_str(dict_: dict) -> str:
    result = "{\n"
    for key, value in dict_.items():
        result += f"    {key} : {value}\n"
    result += '}'
    return result 

if __name__ == "__main__":
    print(convert_dict_to_json_str( {
            "addr" : "127.0.0.1",
            "host" : "8080",
            "route" : "/dev/api/images/get_image",
        }
    ))
    print_list(generator_inertation(0, 10))
