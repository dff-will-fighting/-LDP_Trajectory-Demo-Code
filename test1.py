import sys
import numpy as np
from function.rappor.agg import *

def sum_list(x,y):
    m = list(map(lambda a,b:a+b,x,y))
    return m


def str2list2int(data):
    Data = np.zeros(278)
    for i in range(len(data)):
        Data = sum_list(map(int,list(data[i])),Data)     #str2list2int 后求和
    return list(map(int,list(Data)))

if __name__ == "__main__":
    point =  list(np.loadtxt('onepoint.txt',dtype=str))
    # print(list(point[0]))       #字符串转列表
    # print(list(map(int,(list(point[0])))))
    # print(list(point))
    # i = list(map(int,list(point[0])))+list(map(int,list(point[1])))+list(map(int,list(point[2])))+list(map(int,list(point[3])))
    # print(i)
    # print(list(map(int,list(point[1]))))
    # print(list(map(int,list(point[0]))))

    num = str2list2int(point)   #[0, 0, 4, 0, 0, 4, 0, 4, 4, 0, 4, 0, 4, 0, 2, 1, 2, 1, 3, 2, 1, 1, 1, 2, 2, 1, 2, 0,
    # C = Aggregation(f=0.5,p =1,q =0,k = 278 ,N =3478176)
    # print(C.eatimata(num,278,3478176))
    print(int(3.8))

    a = '01010010101011101001'
    a1 = list(a)
    a1[5] = '2'
    a = ''.join(a1)
    print(a)