def subtract_all(x: list[float], y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = 5
    # restituisce [-4,-3,-2,-1,0]

    l: list[float] = [] # oppure lista vuota con list()
    for elem in x:
        diff: float = elem - y
        l.append(diff)
    return l

mylist: list[float] = [1,2,3,4,5]
y: float = 10
result = subtract_all(mylist, y)
print(f'Il risultato è {result}')