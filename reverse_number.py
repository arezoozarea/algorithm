a = -56


def reverse_number(number):
    if number > 0:
        num_component = [x for x in str(number)]
        num_str = "".join(num_component[::-1])
        num_number = int(num_str)
    else:
        number = abs(number)
        num_component = [x for x in str(number)]
        num_str = "".join(num_component[::-1])
        num_number = -abs(int(num_str))
    return num_number

print(reverse_number(7654))