def palindrome_check(temp_list):
    palindrome_list = []
    reverse = int(len(temp_list)-1)
    for index in range(len(temp_list)):
        if temp_list[index] != temp_list[reverse]:
            # print(temp_list," is not a palindrome")
            return 0
        elif index == int(len(temp_list)/2) and index > 0:
            # print(temp_list, " is a palindrome.")
            temp_list = ''.join(temp_list)
            palindrome_list.append(temp_list)
        reverse-=1

    # print(palindrome_list)
    return palindrome_list

if __name__=="__main__":
    string = "abaccaba"
    temp_list = []
    palindrome_list = []
    index2= 0
    string_count = len(string)-1
   
    for index in range(len(string)):
        index2 = index+1
        temp_list.append(string[index])

        while index2 <= len(string)-1:
            temp_list.append(string[index2])
            result = palindrome_check(temp_list)
            # print(result)
            if result != 0:
                # print(result)
                palindrome_list.append(result)
                # print(palindrome_list)
            index2+=1
        temp_list = []
    # print(palindrome_list)
    for index in range(len(palindrome_list)):
        print(palindrome_list[index], len(palindrome_list[index]))
        

    