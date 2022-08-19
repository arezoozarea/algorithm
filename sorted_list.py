# a = [2, 5, 3, 9, 2, 1]
# new_list = []
# aa = np.array(a)
# unique = False
# small_num = aa[0]
# print(small_num)
# # bb =pd.DataFrame(aa)
# for i in aa:
#     if i<small_num:
#         small_num =i
#     new_list.append(i)
# print(new_list)
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
minimum = data_list[0]
for i in range(len(data_list)):
    for j in range(i + 1, len(data_list)):
        if data_list[i] > data_list[j]:
            data_list[i], data_list[j] = data_list[j], data_list[i]
print(data_list)
