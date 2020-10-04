# Generate the largest perfect number smaller than a given natural number n. 
# If such a number does not exist, a message should be displayed. 
# A number is perfect if it is equal to the sum of its divisors, 
# except itself. (e.g. 6 is a perfect number, as 6=1+2+3).


def is_perfect(n):
    """Returns whether n is a perfect number"""
    sum = 0

    for d in range(1, n):
        if n % d == 0:
            sum += d

    return sum == n


def get_user_input():
    """Returns the first valid integer input from the user"""
    while True:
        print('Generate the largest perfect number, smaller than: ', end='')
        
        try:
            return int(input())
        except:
            print('An error occurred. Try again!\n')


def solve():
    """Solves the problem"""
    n = get_user_input()

    for i in range(n - 1, 0, -1):
        if is_perfect(i):
            print("The result is:", i)
            return

    print("No such number was found")


if __name__ == '__main__':
    solve()

