if __name__ == '__main__':
    print("Enter no of commands:")
    N = int(input())
    lists = []
    
    for i in range(N):
        command = input().split()
        # print("command: ", command[0])
        if int(command[0]) == 1:
            lists.append(i)
        elif int(command[0]) == 2:
            print(lists)
        elif int(command[0]) == 3:
            lists.remove(i)
        elif int(command[0]) == 4:
            lists.append(i)    
        elif int(command[0]) == 5:
            lists.sort()
        elif int(command[0]) == 6:
            lists.pop()
        elif int(command[0]) == 7:
            lists.reverse()
        else:
            print("Invalid")
        
