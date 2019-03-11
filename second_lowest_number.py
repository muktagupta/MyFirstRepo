
#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.



if __name__ == '__main__':
    student_list=[]
    temp_name=[]
    n= int(input()) #collect n
    
    if (n >=2 and n<=5):
        for i in range(n):
            name = input()
            score = float(input())
            temp=[name,score]
            student_list.append(temp)
    else:
            print ("n is Invalid")
            exit()

    #get the second lowest number
    low1=student_list[0][1]
    low2=student_list[0][1]
    for i in range(n):
        if (student_list[i][1] < low1):
            low2= low1
            low1= student_list[i][1]
        if student_list[i][1]> low1 and ( student_list[i][1]<low2 or low1==low2):
            low2= student_list[i][1]
            
    # now create list of names having second lowest number 
    for i in range(n):
        if student_list[i][1]== low2:
            temp_name.append(student_list[i][0])
            
    #if more than 1 student have second lowest number then print names in alphabetical order
    temp_name.sort()
    for i in temp_name:
        print(i)














