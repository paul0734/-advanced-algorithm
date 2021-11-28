arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]

row=0

for i in range(0,len(arr1)):
    row = arr1[i] | arr2[i]
    print("[", end="")
    for j in range(len(arr1)-1,-1,-1):
        if(((row >> j )& 1 ) ==1 ):
            print("#", end="")
        else:
            print(" ", end="")
    print("]")
