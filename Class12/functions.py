def add(a:int,b:int,c:int = 2)-> tuple[float,float]:
    return float(a+b+c) , float(a-b-c)

x,y = add(1,2,3)
print(x,y)