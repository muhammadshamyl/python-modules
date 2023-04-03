import random
if __name__=="__main__":
    number = 2#int(input("Enter input: "))
    length = number
    parenthesis_list = []
    parenthesis = []
    left = 0
    right = 0
    counter = 0
    parenthesis.append("(")
    left +=1
    while left != right and counter != number:
        while left < length:
            if right == length:
                parenthesis.append(")")
                right +=1
            decider = random.randint(0,1)
            print("decider: ", decider)
            if decider == 0 and left < number:
                parenthesis.append("(")
                left+=1
            elif decider == 1 and right < left:
                parenthesis.append(")")
                right+=1
            if left == right:
                counter +=1
        parenthesis_list.append(parenthesis)
                
    for item in parenthesis_list:
        print(item)