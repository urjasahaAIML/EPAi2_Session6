import pytest
import random
import string
import math
from session_6_closures import *


def test_docstring_meter_1():
    
    def myfunc():        
        '''this is s docstring so less characters long'''
        pass
    
    f=docstring_meter(50)
    assert (not f(myfunc)),'docstring is >= 50 characters'
    

def test_docstring_meter_2():
    
    def myfunc():        
        '''this is s docstring so many characters long aba dabba du aba dabba du aba dabba du 
        aba dabba du aba dabba du aba dabba du aba dabba du aba dabba du'''
        pass

    f=docstring_meter(50)
    assert f(myfunc), 'docstring is not >= 50 characters'
    

def test_docstring_meter_None_3():
    
    def myfunc():       
        pass

    f=docstring_meter(50)
    assert not f(myfunc), 'docstring is not >= 50 characters'
    
    
def test_docstring_meter_invalid_size_4():
    
    def myfunc():       
        pass
    
    with pytest.raises(ValueError):
        f=docstring_meter(-1)
        assert not f(myfunc), 'docstring is not >= 50 characters'

##############################################################
    
def test_next_fib_1():
    f = next_fib()
    assert f() == 1, 'incorrect fibonacci'
    assert f() == 1, 'incorrect fibonacci'
    assert f() == 2, 'incorrect fibonacci'
    assert f() == 3, 'incorrect fibonacci'
    assert f() == 5, 'incorrect fibonacci'
    assert f() == 8, 'incorrect fibonacci'
    
##############################################################    

def test_count_invoke():
    def add(a, b):
        pass

    def mult(a, b):
        pass

    def div(a, b):
        pass
    
    def printme(*args):
        pass

    counted_add = count_invoke(add)
    counted_mult = count_invoke(mult)
    counted_div = count_invoke(div)
    counted_printme = count_invoke(printme)
    
    counted_add(10,20)
    counted_add(11,21)
    counted_mult(5,6)
    counted_div(5,6)
    counted_mult(15,6)
    counted_printme('hi there')
    
    assert counters['add'] == 2 and counters['mult'] == 2 and \
        counters['div'] == 1, 'counter did not work' and \
           counters['counted_printme'] == 1 
    
############################################################## 


def test_count_dict():
    def add(a, b):
        pass

    def mult(a, b):
        pass

    def div(a, b):
        pass
    
    def printme(*args):
        pass
    
    dict_apples = dict()
    dict_oranges = dict()

    counted_add = counter_dict(add, dict_apples)
    counted_mult = counter_dict(mult, dict_apples)
    counted_div = counter_dict(div, dict_apples)
    counted_printme = counter_dict(printme, dict_oranges)
   
    counted_add(10,20)
    counted_add(11,21)
    counted_mult(5,6)
    counted_div(5,6)
    counted_mult(15,6)
    counted_printme('hello there')

    assert dict_apples['add'] == 2 and dict_apples['mult'] == 2 and dict_oranges['printme'] == 1
    