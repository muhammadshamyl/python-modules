if __name__=="__main__":
    lis = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sum = []
    sum_count = 0
    for index in range(len(lis)):
        # print(lis[index])
        for index2 in range(len(lis[index])):
            # print("Inner loop: ", lis[index][index2])
            sum_count += lis[index][index2]
        sum.append(sum_count)
        sum_count = 0
    print(sum)
    highest = 0
    for index in range(len(sum)):
        if highest < sum[index]:
            highest = sum[index] 
    print(highest)