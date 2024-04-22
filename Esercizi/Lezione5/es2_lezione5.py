def subtract_all(x: list[float], y: float): # -> list[float] non va scritto perchè non si usa return
    # x = [1,2,3,4,5]
    # y = 5
    # risultato [-4,-3,-2,-1,0]
    
    for i in range(len(x)):
        x[i] -= y
    # return x è superfluo, a meno che si richiede di restituire la lista. 

mylist: list[float] = [1,2,3,4,5]
y: float = 10
result = subtract_all(mylist, y)
print(f'Il risultato dopo la sottrazione è {mylist}')