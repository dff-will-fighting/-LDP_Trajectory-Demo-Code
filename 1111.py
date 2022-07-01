# -*- coding:UTF-8 -*-
"""
作者：付露芬
日期：2021年月17日

"""
import h5py
if __name__ == '__main__':

    mat = h5py.File("BJ_FLOW.h5","r")
    print(mat.keys())
    # print(mat['embeddings'])
    # print(mat['embeddings'][:])
    # print(mat['date'])
    m = mat['data']
    print(m[:])
    print(m)
    # # n = mat["loninTP"][:]