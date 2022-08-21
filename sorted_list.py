data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
unique_list = []
data_dict = {i: data_list.count(i) for i in data_list}
for data in data_dict:
    if data not in unique_list:
        unique_list.append(data)
minimum = unique_list[0]
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):
        if unique_list[i] > unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]
print(unique_list)
