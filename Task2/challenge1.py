# Get the nth number in the fibonacci sequence given n
def fibonacci(n):
    if n <= 2:
      return n - 1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

# Given a number F, print out whether it's a fibonacci number and what the closest index n in the fibonacci sequence is.
fibonacci_ls = [0, 1]
def is_fabonacci(n):

    while(fibonacci_ls[-1] < n):
        fibonacci_ls.append(fibonacci_ls[-1]+fibonacci_ls[-2])
  
    if fibonacci_ls[-1] == n:
        return "{} is a fibonacci number with index {}".format(n, len(fibonacci_ls)-1)

    return "The index of closest fibonacci number of {} is {}".format(n, len(fibonacci_ls) -(2 if fibonacci_ls[-1] - n > n - fibonacci_ls[-2] else 1))
