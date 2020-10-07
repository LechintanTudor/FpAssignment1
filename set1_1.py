"""
Generate the first prime number larger than a given
natural number `n`.
"""
import sys


def find_prime_greater_than(n):
    """Returns the first prime integer greater than `n`."""
    value = n + 1   
    while True:
        if is_prime(value):
            return value

        value += 1
 

def is_prime(n):
    """Returns whether or not the integer `n` is prime."""
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


def test_find_prime_greater_than():
    """Tests for `find_prime_greater_than` function"""
    assert find_prime_greater_than(-5) == 2
    assert find_prime_greater_than(12) == 13
    assert find_prime_greater_than(42) == 43


def test_is_prime():
    """Tests for `is_prime` function"""
    assert is_prime(2)
    assert is_prime(13)
    assert is_prime(43)

    assert not is_prime(-1)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(25)


def run_tests():
    """Runs all tests."""
    test_is_prime()
    test_find_prime_greater_than()
    print("All tests passed!")


def solve_problem():
    """Solves the problem."""
    n = get_user_input()
    value = find_prime_greater_than(n)
    print("The result is:", value)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '--test':
        run_tests()
    else:
        solve_problem()

