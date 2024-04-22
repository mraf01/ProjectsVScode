""" 
    esempio:
    x = [1,2,3,4,5]
    y = [2,4,8,10,7]

    sottrazione tra gli elementi delle liste x e y
    
    restituisce [-1,-2,-5,-6,-2] e quando una delle liste è più lunga 
    restituisce lo stesso [-1,-2,-5,-6,-2] quindi gli indici fuori dal range vengono esclusi.
"""

def add_diff_to_res(x: list[float], y: list[float], length: int) -> list[float]:
    res: list[float] = []
    for i in range(length):
        res.append(x[i] - y[i])
    return res

def subtract_lists(x: list[float], y: float) -> list[float]:
    length = min(len(x), len(y))
    res: list[float] = add_diff_to_res(x, y, length)
    return res

list1: list[float] = [1,2.5,3,4,5,8]
list2: list[float] = [2,4,8,10,7]
result = subtract_lists(list1, list2)
print(f'Il risultato dopo la sottrazione è {result}')