# arr = [1, 3, 5, 7, 9]



def miniMaxSum(arr):
    total_sum = []
    for i in range(len(arr)):
        befor_number = arr[:i]
        after_num = arr[i + 1:len(arr)]
        total_num = befor_number + after_num
        total_sum.append(sum(total_num))
    print(str(min(total_sum)) + "  " + str(max(total_sum)))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
