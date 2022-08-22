data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
data_dict = {i: data_list.count(i) for i in data_list}
for data in data_dict:
    print (data_dict[data])