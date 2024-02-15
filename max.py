"""
How many ways are there to compute the maximum of three numbers?
"""



def basic(a: int, b: int, c: int) -> int:
    """
    Basic way.
    """

    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c



def noob(a,b ,c): 
    #Hello, I'm 17 and learning Python!
    #check a 
    if a >b: 
        if a  > c:
            max = a
        if c> a:
            max =c
        if a ==  c:
            max=a #i like a
    #check b
    if b > a:
        if b >c:
            max = b 
        if c > b:
            max = c
        if b ==c:
            max = b 
    #check c
    if c>a:
        if c>b: 
            max = c
        if b> c:
            max =b
        if c ==b:
            max=  b
    return max 



def oneliner(a: int, b: int, c: int) -> int:
    """
    No one can understand it, but it looks complicated.
    """
    return (a if a > b else b) if b > c else (a if a > c else c)



def sorting(a: int, b: int, c: int) -> int:
    """
    Faster than any other purely Python implementation.
    """

    return [a, b, c].sort()[0]



def python_is_not_a_programming_language(a: int, b: int, c: int) -> int:
    """
    Using Python as a C interface, as God intended.
    """

    return max(a, b, c)



def napper(a: int, b: int, c: int) -> int:
    """
    I like to sleep, and I'm not afraid of threads.
    """
    import threading
    import queue
    from time import sleep

    # queue for workers
    worker_queue = queue.Queue()

    def _napper_work(n: int):
        sleep(n)
        worker_queue.put(n)

    # create threads
    threads = [ threading.Thread(target=_napper_work, args=(i,), daemon=True) for i in (a, b, c) ]

    # run threads
    for th in threads:
        th.start()

    # this will block until the first element is in the queue
    return worker_queue.get()



def recursion(*values) -> int:
    """
    You've just learnt what recursion is.
    """

    if len(values) == 1:  # base case
        return values[0]
    else:
        max = recursion(*values[1:])

        return max if max > values[0] else values[0]



def functional(a: int, b: int, c: int) -> int:
    """
    Functional programming rules!
    """
    from functools import reduce

    return reduce((lambda x, y : y if y > x else x), [a, b, c])

