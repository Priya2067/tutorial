def factorial(n):
    """
    Ye function factorial of n return karta hai
    """
    if n == 1: # base case
        return 1
    else:
        return n * factorial(n - 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ans = factorial(3)
    print(f"answer = {ans}")
