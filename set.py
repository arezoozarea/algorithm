

a = [2,6]
b = [24,36]
c= len(b)


number_list = []
# result = [["1", "1", "1", "1"], ["1", "1", "1", "1"]]
# print('\n'.join([' '.join(map(str, x)) for x in result]))
# for i in range(len(a)):
#     if max(a)% a[i]==0:
#         print((max(a)*2)*(c))
#

n= 80
for i in range(n):
    if i == 0 or i == n-1:
        print(("*"+" ")*n)
    else:
        print("*" + " "*(((n-2) *2)+1) +"*")
