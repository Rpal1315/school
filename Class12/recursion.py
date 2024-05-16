def gcd(a:int,b:int)-> int:
    """
    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of the two integers.
    """
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def fibo(n:int)-> int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def binsearch(arr:list[int],key:int,low:int,high:int)-> int:
    arr.sort()
    if low>high:
        return -1
    mid = (low+high)//2
    if key == arr[mid]:
        return mid
    elif key > arr[mid]:
        low = mid +1
        return binsearch(arr,key,low,high)
    else:
        high = mid - 1
        return binsearch(arr,key,low,high)
if __name__ == '__main__':
    arr = [3,2,5,1,12,9,34]
    print(binsearch(arr,9,0,len(arr)-1))


