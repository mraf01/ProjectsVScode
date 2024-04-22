def subtract_lists(x: list[float], y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = [2,4,8,10,7]
    # restituisce [-1,-2,-5,-6,-2]

    l: list[float] = []
    for i in range(len(x)):
        l.append(x[i] - y[i])
    # i: int = 0
    # while i < len(x):
    #   l.append(x[i] - y[i])
    #   i += 1
    return l

list1: list[float] = [1,2,3,4,5]
list2: list[float] = [2,4,8,10,7]
result = subtract_lists(list1, list2)
print(f'Il risultato dopo la sottrazione è {result}')