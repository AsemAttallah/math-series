def fibonacci(n):
    '''
    This function to calculate fibonacci sequence numbers
    :param: n (int)
    :return: (int)
    '''
    if n==0:
        return 0
    if n==1:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    '''
    This function to calculate lucas sequence numbers
    :param: n (int)
    :return: (int)
    '''
    if n==0:
        return 2
    if n==1:
        return 1
    else :
        return lucas(n-1)+lucas(n-2)


def sum_series(n,x=0,y=1):
    '''
    This function work like fibonacci fun but here we can change base case
    :param: n, x, y (int)
    :return: (int)
    '''
    if x==0 and y==1:
        if n==0:
            return 0
        if n==1:
            return 1
        else :
            return sum_series(n-1)+sum_series(n-2)
    
    if x!=0  or y!=1:
        if n==0:
            return x
        if n==1:
            return y
        else :
            return sum_series(n-1,x,y)+sum_series(n-2,x,y)
    
