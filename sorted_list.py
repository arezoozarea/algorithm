data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
data_dict = {}
unique_list = []
def sorted_list(input_list):
    for data in input_list:
        if data not in data_dict:
            data_dict[data] = True
            unique_list.append(data)
            for i in range(len(unique_list)):
                for j in range(i + 1, len(unique_list)):
                    if unique_list[i] > unique_list[j]:
                        unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

    return unique_list

print(sorted_list([-5, -23, 5, 0, 23, -6, 23, 67]))
