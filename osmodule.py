# import os
# if (not os.path.exists("data")) :
#  os.mkdir("data")
# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")
import os
for i in range(0,100):
    os.rename(f"data/tut{i+1}",f"data/Day{i+1}")
# #--------------------------local global scope variable----------
# x=5
# def hnji():
#     global x
#     x=6
#     print(x)   
# hnji()
# print(x)