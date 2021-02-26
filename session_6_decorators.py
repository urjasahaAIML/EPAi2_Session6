import time
from functools import wraps

# decorator odd_sec ###################

def odd_sec(fn:callable):    
    ''' decorator for executing function in odd seconds '''
    
    from math import trunc
    
    
    @wraps(fn)
    def inner(*args, **kwargs):   
        ''' closure that checks time and executes function '''
        
        now_in_sec = trunc(time.time())      
        if now_in_sec % 2 == 1: # odd second   
            result= fn(*args, **kwargs)                
            return f'\nsecond is odd({now_in_sec}).successfully executed "{fn.__name__}()": result= {result}'        
        else:
            return f'\nsecond is even({now_in_sec}).can not execute "{fn.__name__}()" function. please try after 1 second\n'
        
    return inner


# decorator logged ###################

def logged(fn):
    ''' decorator to add log '''
    
    from datetime import datetime, timezone    
    
    @wraps(fn)
    def inner(*args, **kwargs):   
        dt = datetime.now(timezone.utc)
        fn(*args, **kwargs) 
        return f'log:{fn.__name__} was executed at {dt}'
        #return result
     
    return inner


# decorator timed n times ###################

def timed_n(n: int):
    
    ''' executes a function n times and counts time taken '''    
    

    def timed(fn: callable)-> callable:
    
        ''' times execeution time of function '''
    
        from time import perf_counter
    
        def inner(*args, **kwargs):   
                    
            ''' measure execuion time '''
            
            if n < 1:
                raise ValueError('n must be > =1')
        
            start = perf_counter()
            for i in range (n+1):
                fn(*args, **kwargs) 
            end = perf_counter() 
            time_taken = end - start
            return f'{time_taken}:{fn.__name__}():{n}: times ms'
            #return time_taken
        return inner
    return timed


# decorator authenticate ###################
global_result = []
def authenticatedOrNot(auth:bool):
    global global_result
    ''' authentication decorator '''
    
    def dec(fn):
        
        ''' execute passed in function '''
        
        def inner(*args, **kwargs):           
            return fn(*args, **kwargs)
        return inner
    
    if (auth):  
        #print("You are successfully authenticated")
        global_result.append("You are authenticated")
        return dec
    else:
        #print("You are not authenticated. need login")
        global_result.append("You are not authenticated")        
        return dec

# decorator authenticate 4 levels ###################

def auth_factory(privelege_level: str):
    
    ''' privelege_level may be high/med/low/no '''

    def singledispatch(fn: callable):
        
        ''' what permission the privelege_level has '''
    
        #all_parameters = ['createfolder', 'createfile', 'editfile', 'readfile']  
        
        registry = dict()    
        registry['high'] = ['createfolder', 'createfile', 'editfile', 'readfile']
        registry['med']  = ['createfile', 'editfile', 'readfile']
        registry['low']  = ['editfile', 'readfile']
        registry['no']   = ['readfile']
    
        @wraps(fn)
        def inner(arg):
            allowed_parameters = registry.get(privelege_level) 
            print(f'parameters accessible with privilege="{privelege_level}" are {allowed_parameters}')           
            if fn.__name__ in allowed_parameters:                
                return fn(arg)    
            else:               
                return f'insuffient previlege for function {fn.__name__} with privilege= {privelege_level}'
        
        return inner
    
    return singledispatch