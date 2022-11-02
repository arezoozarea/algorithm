def is_leap(year):
    leap = False

    # Write your logic here
    if year >= 1900 and year <= 10 ^ 5 and year%4==0 and year%100==0 and year%400==0:

        leap=True

    return leap


# year = int(input("1950"))
print(is_leap(1950))