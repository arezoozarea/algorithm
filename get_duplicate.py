
def get_duplicate(str_list):
    unique_list = []
    duplicate_list = []
    char_list = [i for item in str_list for i in item]
    my_dict = {i: char_list.count(i) for i in char_list}
    # for item in char_list:
    #     if item not in d_dict:
    #         d_dict[item] = (char_list.count(item))
    #     else:
    #         d_dict[item] =(char_list.count(item))
    for item in my_dict:
        if my_dict[item] == 1:
            unique_list.append(item)
    return unique_list

    # for item in char_list:
    #     if char_list.count(item)>1:
    #         duplicate_list.append(item)
    # print(duplicate_list)
print(get_duplicate(["Cart", "local", "data", "dentist", "noon", "bravo"]))