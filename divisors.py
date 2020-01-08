# Question
# The number of divisors of 120 is 16. In fact 120 is the smallest number having 16 divisors. Find the smallest number with 2500500 divisors. Give your answer modulo 500500507.

# from a simple calculation I found that
# number of divisors          smallest number           power of 2               
#        1  (2**0)            factorial(0+1) = 1               0                         
#        2  (2**1)            factorial(1+1) = 2               1             
#        4  (2**2)            factorial(2+1) = 6               2             
#        8  (2**3)            factorial(3+1) = 24              3              
#        ...                         ...                       ...               
#        ...                         ...                       ...               
#        (2**500500)          factorial(500500+1) =         500500               


def factorial(n):
    value = 1
    while n != 1 :
        value *= n
        n -= 1
        print(n)
    return value

print(factorial(5005001))


# A genuine solution Explanation

# if n is the required number
# number of divisors of n = 2**500500
# 2**500500 means, it has at-most 500500 unique prime factors(p1, p2, p3, ....pt)
# And n = p1**e1 * p2**e2 * p3**e3 * .... pt**at where a1, a2, c are the powers of prime factors -------------------(equation 1)
# Also, (e1+1)(e2+1)(e3+1)...(et+1) = 2**500500
# The powers of prime factors should be so chosen that the equation 1 gives smallest value
