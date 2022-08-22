def calculate_hash(numbers):
    first_value = 97
    last_value = 122
    hash_dict = {}
    number_range = [i * 4 if i % 2 == 0 else i * 3 for i in numbers]
    for number in number_range:
        hash_num = number + 97
        if hash_num > 122:
            hash_num = (hash_num - last_value) + first_value
        hash_dict[chr(hash_num)] = number
    return (hash_dict)


def flat_hash(numbers):
    hash_result = []
    integrate_numer_list = [i for item in numbers for i in item]
    for item in integrate_numer_list:
        hash_result.append(get_hash_id(item))
    return hash_result


def get_hash_id(number):
    hash_dict = {}
    hash_num = number + 97
    if hash_num > 122:
        hash_num = (hash_num - 122) + 97
    hash_dict[chr(hash_num)] = number
    return hash_dict


def main():
    print (flat_hash([[25, 30], [12, 40]]))


if __name__ == '__main__':
    main()
