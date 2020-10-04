# Generate the first prime number larger than a given
# natural number n.


def find_prime_greater_than(n):
    """Returns the first prime integer greater than n."""
    value = n + 1   
    while True:
        if is_prime(value):
            return value

        value += 1
 

def is_prime(n):
    """Returns whether or not the integer n is prime."""
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        
        d += 2

    return True


def get_user_input():
    """Returns the first valid integer input from the user."""
    while True:
        print('Find the first prime integer greater than: ', end='')
        
        try:
            return int(input())
        except:
            print('An error occurred. Try again!\n')


def solve():
    """Solves the problem."""
    n = get_user_input()
    value = find_prime_greater_than(n)
    print("The result is:", value)

if __name__ == '__main__':
    solve()

