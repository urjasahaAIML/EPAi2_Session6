# EPAi2_Session6

# Closures:

link:  https://github.com/urjasahaAIML/EPAi2_Session6/blob/main/session_6_closures.py

## Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 

docstring_meter(size:int) -> 'a closure'  

## Write a closure that gives you the next Fibonacci number 

next_fib():


## We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts 

count_invoke(fn: callable)-> callable

## Modify above such that now we can pass in different dictionary variables to update different dictionaries 

counter_dict(fn : callable , fn_counter : dict) -> callable



# Decorators:

link: https://github.com/urjasahaAIML/EPAi2_Session6/blob/main/session_6_decorators.py


## allows a function to run only on odd seconds 

odd_sec(fn:callable):

## log 

logged(fn):


## timed (n times) 

timed_n(n: int):

## authenticate 

authenticatedOrNot(auth:bool):


## Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) 

auth_factory(privelege_level: str):


