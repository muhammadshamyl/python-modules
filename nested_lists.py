if __name__=="__main__":
    score_list = [['shamyl',50],['Ali',50],['Zafar',60],['Aqeel',70],['Dua',100],['Durrani',60],['Alpha',90],['Beta',85],['Gamma',60],['Delta',70]]
    score_list = sorted(score_list,key=lambda x:x[1])
    print(score_list)
    temp = None
    counter=0
    second_lowest_score = None
    second_lowest_studentsList = []
    for current_index in range(len(score_list)-1):
        print(score_list[current_index])
        if score_list[current_index][1] < score_list[current_index + 1][1]:
            second_lowest_score = score_list[current_index][1]
            counter = counter + 1
        if counter == 2:
            break
    print(second_lowest_score)
    for x in score_list:
        print(x[1])
        if x[1] == second_lowest_score:
            second_lowest_studentsList.append(x)
    print(second_lowest_studentsList)    
    second_lowest_studentsList2 = []    
    second_lowest_studentsList2 = sorted(second_lowest_studentsList, key=lambda x: x[0])    
    print(second_lowest_studentsList2)    
