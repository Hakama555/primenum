def prime_num(var):
    import numpy as np
    n = int(np.sqrt(var))  # エラストテネスのふるいよりその数の√を求める
    array = np.ones(var + 1, dtype = "int8")  # np.onceで１が欲しい数個ある配列を作る
    for an_1 in range(2, var + 1):  # 配列の中で素数で無い物を０に置き換える
        for an_2 in range(an_1 + an_1, var + 1, an_1):  # 
            array[an_2] = 0
    count = 0
    for j in array:
        if j == 1:
            count += 1  # 残った１を数える
    print(count)
var = 1000  # 欲しい数字の上限
prime_num(var)
# for j in range(2, n + 1):
#    for k in list:
        
