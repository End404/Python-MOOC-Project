# ********************* 二维数据的处理 ********************* #

# 逐一处理：采用二层循环
ls = [ [1,2], [3,4], [5,6], [7,8] ]    # 二维列表

for row in ls:
    for co in row:  # co：column(列)
        print(co)
        print(row)
        
print( )
print(ls)
print(co)
