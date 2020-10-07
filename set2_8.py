"""
Find the smallest number m from the Fibonacci sequence,  
defined by f[0]=f[1]=1, f[n]=f[n-1]+f[n-2], for n>2, larger 
than the given natural number n. (e.g. for n = 6, m = 8).
"""
import sys


def fibonacci():
    """Returns a Fibonacci sequence generator."""
    yield 1
    yield 1

    previous = [1, 1]
    i = 0

    while True:
        value = previous[0] + previous[1]
        previous[i % 2] = value
        i += 1
        yield value


def get_user_input():
    """Returns the first valid integer input from the user."""
    while True:
        print('Find the smallest number from the Fibonacci set, greater than: ', end='')
        
        try:
            return int(input())
        except:
            print('An error occurred. Try again!\n')


def test_fibonacci():
    """Tests for `fibonacci` function"""
    generator = fibonacci()
    assert next(generator) == 1
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 5
    assert next(generator) == 8
    assert next(generator) == 13


def run_tests():
    """Runs all tests."""
    test_fibonacci()
    print("All tests passed!")


def solve_problem():
    """Solves the problem."""
    n = get_user_input()

    for i in fibonacci():
        if i > n:
            print("The result is:", i)
            break


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '--test':
        run_tests()
    else:
        solve_problem()

