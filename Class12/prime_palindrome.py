# Create a function that checks if a no. is a prime palindrome or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_prime_palindrome(num):
    # Convert the number to a string
    num_str = str(num)

    # Reverse the string
    reverse_str = num_str[::-1]

    # Convert the reversed string back to an integer
    reverse_num = int(reverse_str)

    # Check if the original number and its reverse are the same
    if num == reverse_num:
        # Check if the original number is prime
        if is_prime(num):
            return True
        else:
            return False
    else:
        return False


if is_prime_palindrome(int(input("Enter a number: "))):
    print("The number is a prime palindrome")
else:
    print("The number is not a prime palindrome")