"""
Generate the largest perfect number smaller than a given natural number n. 
If such a number does not exist, a message should be displayed. 
A number is perfect if it is equal to the sum of its divisors, 
except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
"""
import sys


def is_perfect(n):
    """Returns whether the integer `n` is a perfect number."""
    sum = 0

    for d in range(1, n):
        if n % d == 0:
            sum += d

    return sum == n


def get_user_input():
    """Returns the first valid integer input from the user."""
    while True:
        print('Generate the largest perfect number, smaller than: ', end='')
        
        try:
            return int(input())
        except:
            print('An error occurred. Try again!\n')


def test_is_perfect():
    """Tests for `is_perfect` function"""
    assert is_perfect(6)
    assert is_perfect(28)
    assert is_perfect(496)

    assert not is_perfect(7)
    assert not is_perfect(10)
    assert not is_perfect(22)


def run_tests():
    """Runs all tests."""
    test_is_perfect()
    print("All tests passed!")


def solve_problem():
    """Solves the problem."""
    n = get_user_input()

    for i in range(n - 1, 0, -1):
        if is_perfect(i):
            print("The result is:", i)
            return

    print("No such number was found")


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '--test':
        run_tests()
    else:
        solve_problem()

