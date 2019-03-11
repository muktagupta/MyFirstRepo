if __name__ == '__main__':
    List_op = []
    commands= []

    N = int(input()) #input Number of commands
    
    for i in range(N):
        temp= input().split()
        rc= temp[0]
        
        if rc=="pop":
            List_op.pop()
        elif rc=="append":
            List_op.append(int(temp[1]))
        elif rc=="insert":
            List_op.insert(int(temp[1]), int(temp[2]))
        elif rc=="remove":
            List_op.remove(int(temp[1]))
        elif rc=="count":
            List_op.count(int(temp[1]))
        elif rc=="sort":
            List_op.sort()
        elif rc=="reverse":
            List_op.reverse()

        elif rc=="print":
            print(List_op)
        else:
            print("INVALID COMMAND") 
             
