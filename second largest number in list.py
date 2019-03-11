if __name__ == '__main__':
    n = 5
    arr =[8,7,6,5,4]
    max1=arr[0]
    max2=arr[0]
    if (n >=2 and n<=10):
        for i in range(n):
            print(arr[i], max1, max2)
            if (arr[i] >max1):
                max2= max1
                max1= arr[i]
            if arr[i]< max1 and ( arr[i]>max2 or max1==max2):
                max2= arr[i]
        print (max2)
    else:
        print ("n is Invalid")
