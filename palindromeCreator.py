def checkPalindrome(number,k):
    left_index = 0
    lis_left = []
    lis_right = []
    right_index = len(number)-1
    print("right index: ", right_index)
    while left_index <= right_index:
        if number[left_index] != number[right_index]:
            number[left_index] = number[right_index] = max(number[left_index],number[right_index])
            lis_left.append(left_index)
            lis_right.append(right_index)
            k-=1
        left_index+=1
        right_index-=1
    palindrome = ''.join(number)
    print("Palindrome created: ", palindrome)
    print("No of steps remaining:",k)
    if k < 0:
        print("Palindrome not possible in given constraint count")
    elif k > 0:
        print("entering palindromeImp func")
        palindromeImp(number,k,lis_left,lis_right)

def palindromeImp(number,k,lis_left,lis_right):
    if k == 1 and len(number)%2 != 0:
        index = int(len(number)/2) 
        number[index] = '9'
    elif k > 1:
        counter = 0
        while counter < len(lis_left) -1:
            left_index = lis_left[counter]
            right_index = lis_right[counter]
            number[left_index] = number[right_index] = '9'
            counter += 1
    
    revised_palindrome = ''.join(number)
    print("revised palindrome: ", revised_palindrome)
if __name__=="__main__":
    n = str(input("Enter number:"))
    k = int(input("No of steps:"))
    lis = list(n)
    print("check")
    checkPalindrome(lis,k)
# def checkPalindrome(number,k):
#     left_index, right_index = 0, len(number)-1
#     lis_left, lis_right = [], []
    
#     while left_index <= right_index:
#         if number[left_index] != number[right_index]:
#             number[left_index] = number[right_index] = max(number[left_index],number[right_index])
#             lis_left.append(left_index)
#             lis_right.append(right_index)
#             k -= 1
        
#         left_index += 1
#         right_index -= 1
        
#         if k < 0:
#             print("Palindrome not possible in given constraint count")
#             return
        
#     revised_palindrome = ''.join(number)
#     print("Palindrome created:", revised_palindrome)
    
#     if k > 0:
#         for i in range(len(number) // 2):
#             if k == 1 and len(number) % 2 != 0 and i == len(number) // 2:
#                 number[i] = '9'
#                 break
#             if k < 2:
#                 break
#             if number[i] != '9':
#                 if i in lis_left or i in lis_right:
#                     number[i] = number[len(number) - 1 - i] = '9'
#                     k -= 2
#                 else:
#                     number[i] = number[len(number) - 1 - i] = '9'
#                     k -= 2
    
#     revised_palindrome = ''.join(number)
#     print("Revised palindrome:", revised_palindrome)

# if __name__ == "__main__":
#     n = input("Enter number:")
#     k = int(input("No of steps:"))
#     lis = list(n)
    
#     checkPalindrome(lis, k)
