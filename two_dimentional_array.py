from statistics import mean

num = [[1, 2, 3, 7], [4, 5, 6, 8]]
a, b = num
sum_list = []
result_list = []

for i in range(len(a)):
    if i != len(a) - 1:
        num_sum = a[i] + b[i + 1]
        sum_list.append(num_sum)

        if i == 0:
            result_list.append(b[0] + num_sum)

        if i == len(a) - 3:
            result_list.append(a[-1] + num_sum)

        if i == len(a) - 2:
            result_list.append(mean(sum_list) + num_sum)

print(result_list)