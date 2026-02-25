def print_list(list_: list) -> None:
    for val in list_:
        print(val)

def linear_insertation(start: int, end: int) -> list:
    list_ = []
    for i in range(start, end, 1):
        list_.append(i)
    return list_

if __name__ == "__main__":
    print_list(linear_insertation(0, 10))
