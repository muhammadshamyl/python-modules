def palindrome(string):
    var = ''
    reverse = len(string)-1
    print("reverse: ", reverse)
    for index in range(len(string)):
        if string[index] == string[reverse]:
            var = var + string[index]
        reverse = reverse - 1
    return var
if __name__=="__main__":
    # string = str(input("Enter string for palindrome: "))
    string = "aabccdedccbaa"
    result = palindrome(string)
    print(result)