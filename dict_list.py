number_dict = dict()
out_dict = dict()

array_list = {1031: [2, 4, 9, 6], 1032: [5, 6]}

for i in range(1, 4):
    for j in range(1, 11):
        if i not in number_dict:
            number_dict[i] = []

        number_dict[i].append(j)

for key in array_list:
    for number in array_list[key]:
        if number % 2 == 0:
            if 'even' not in out_dict:
                out_dict['even'] = {}
            if key not in out_dict['even']:
                out_dict['even'][key] = []
            out_dict['even'][key].append(number)

        else:
            if 'odd' not in out_dict:
                out_dict['odd'] = {}
            if key not in out_dict['odd']:
                out_dict['odd'][key] = []
            out_dict['odd'][key].append(number)

print(out_dict)
