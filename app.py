import numpy as np
# You can do the test for the medium.txt or easy.txt ..etc just change the open file  in line 3
with open("hard.txt", 'r') as Mtx:  
    Matrix = [[int(num) for num in line.split()] for line in Mtx]

firstLine =  Matrix[0]
N = firstLine[0]
M = firstLine[1]
Q = firstLine[2]

""" main rectangle """
arr = []
for x in range(1,N+1):
    arr.append(Matrix[x])


# corners of subArraies
s=N+1 ; r=0 ; c=0 ; l =s+Q
""" cor_s & cor_e are lists to store the upper left and lower right corners for each rectangle """
cor_s=[]   
cor_e=[] 
for idx in range(s , l):
    cor_s.append(Matrix[idx][0])
    cor_s.append(Matrix[idx][2])
    cor_e.append(Matrix[idx][1])
    cor_e.append(Matrix[idx][3])


def subArr(start_r,start_c,end_r,end_c):
    sublist = [] ; list=[]
    for idx_r in range(start_r-1,end_r):
        for idx_c in range(start_c-1,end_c):
            sublist.append(arr[idx_r][idx_c])
        list.append(sublist)
        sublist = []

    sub=np.array(list)    
    min = sub.min()
    max = sub.max()
    mx = [min,max]
    return mx




if __name__ == "__main__":

    l = Q * 2 ; max_min=[]
    for idx in range(0,l,2):
      max_min += [subArr(cor_s[idx],cor_s[idx+1],cor_e[idx],cor_e[idx+1])]

    for i in range (len( max_min)):
        print( max_min[i][0], max_min[i][1])









