from math import factorial


# def fn():
#     '''global n'''
#     n= int(input('enter a number: '))
#     x=factorial(n)
#     print(x)
#
# fn()


def fn():
    '''global n'''
    n= int(input('enter a number: '))
    N=n
    x=1
    while n>1:
        x*=n
        n=n-1
    print('Factorial of '+str(N)+ ' is: ' +str(x))
fn()