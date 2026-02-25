def print_list(list_: list) -> None:
    for val in list_:
        print(val)

if __name__ == "__main__":
    list_of_smth = []
    for i in range(0, 10, 1):
        list_of_smth.append(i)

    print_list(list_of_smth)
