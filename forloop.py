
fruits = ['apple','banana','orange']

#Simple for loop
for x in fruits:
    print(x)
#alternate
print("\nalternate \n")
for x in range(len(fruits)):
    print (fruits[x])


#to split an array item and print it bit by bit 
for x in fruits[1]:
    print(x)

#nested loop that traverses through each item and prints it alphabet by alphabet
for x in fruits:
    for y in x:
        print(y)

    
#for loop with else
for x in fruits:
    print(x)
else:
    print("End of list")

#example
student_name = "Shamyl"
marks = {'Ali':30,'Asghar':50,'Adnaan':100}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print(student_name, " not found in the provided list.")