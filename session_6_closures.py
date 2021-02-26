#1 ##############################################
def docstring_meter(size:int) -> 'a closure' :  
    
    ''' checks the length of inner function'''
            
    def inner(fn: str)-> bool:   
        
        ''' the closure that is attached  with 1 free var ''' 
        if size < 1:
            raise ValueError('size must be > =1')
        
        if not fn.__doc__:
            return 0 > size
        return len(fn.__doc__) > size    
    return inner


# 2 ##############################################

def next_fib():
    
    ''' generate next fibonacci number \
        i.e. first call returns 1 \
             second call return 2'''
             
    n = 0 #initalize
    fibs = [0,1,1]
    
    def inner(): 
        ''' the closure that is attached  with 2 free vars '''
        
        nonlocal n, fibs        
        n += 1
        if n <= 2:
            return fibs[n]
        else:            
            fibs.append(fibs[n-1] +  fibs[n-2])
            return fibs[n]       
    return inner


# 3  ##############################################

counters = dict()

def count_invoke(fn: callable)-> callable:    
    ''' keeps count how many times add/mult/div func was invoked '''
    
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        ''' the closure that is attached  with 1 free var '''
        
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)
    
    return inner

def add(a, b):
    ''' vanilla add function'''
    return a + b

def mult(a, b):
    ''' vanilla mult function'''
    return a * b

def div(a, b):
    ''' vanilla div function'''
    return a/b


# 4  ##############################################

def counter_dict(fn : callable , fn_counter : dict) -> callable:    
    ''' keeps count how many times add/mult/div func was invoked '''
    
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        ''' the closure that is attached  with 1 free var '''
        
        nonlocal cnt, fn_counter
        cnt = cnt + 1
        fn_counter[fn.__name__] = cnt 
        return fn(*args, **kwargs)
    
    return inner



#  Decorators   ##############################################