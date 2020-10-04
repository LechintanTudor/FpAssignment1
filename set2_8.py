# Find the smallest number m from the Fibonacci sequence,  
# defined by f[0]=f[1]=1, f[n]=f[n-1]+f[n-2], for n>2, larger 
# than the given natural number n. (e.g. for n = 6, m = 8).


def finbonacci():
    """Returns a Fibonacci sequence generator."""
    previous = [1, 1]
    yield previous[0]
    yield previous[1]

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


def solve():
    """Solves the problem."""
    n = get_user_input()

    for i in finbonacci():
        if i > n:
            print("The result is:", i)
            break


if __name__ == '__main__':
    solve()

