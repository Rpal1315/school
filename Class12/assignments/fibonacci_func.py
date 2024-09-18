def cal(n:int)-> int:
    """
    The function calculates the sum of Fibonacci numbers up to a specified number of terms.
    
    :param n: The parameter `n` in the `cal` function represents the number of terms in the Fibonacci
    sequence that you want to calculate. The function calculates the Fibonacci number at the `n`th
    position in the sequence
    :type n: int
    :return: The function `cal(n)` is returning the nth Fibonacci number.
    """
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
