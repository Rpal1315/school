def is_prime(n: int) -> bool:
    """
    Returns True if the input is prime, False otherwise.
    """
    factors = []
    # Find all factors of the input number
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)

    # Check if the factors are only 1 and the input number itself
    if factors == [1, n]:
        return True
    else:
        return False
