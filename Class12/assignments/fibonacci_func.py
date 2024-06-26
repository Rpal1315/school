def cal(n:int)-> int:
    if n == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(n-1):
            a,b = b,a+b

        
        return int(b)

inp = int(input("Enter the no. of terms to calculate.: "))

print("The sum of fibonacci numbers upto",inp,"is",cal(inp))
