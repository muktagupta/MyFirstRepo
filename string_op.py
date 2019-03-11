#Given a string S of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

#Input Format
#The first line contains an integer, T (the number of test cases). 
#Each line i of the T subsequent lines contain a String, S.

#Input : Mukta
#output: Mka ut



if __name__=='__main__':
    n= int(input())
    list_str=[]
    list_test=[]
    for i in range(n): #input strings on the basis of input entered.
        str1= input()
        list_str.append(str1)

    for i in list_str:
        list_test= list(i) #convert strings entered into words
        for i in range(len(list_test)):
            if i%2==0:
                print (list_test[i], end = "")
        print(" ", end ="")
        for i in range(len(list_test)):
            if i%2==1:
                print (list_test[i], end = "")
        print(end="\n")
                
    
    
