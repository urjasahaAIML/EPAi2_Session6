import pytest
import random
import string
import math
import time
from session_6_decorators import *

def test_odd_sec_1():
    
    @odd_sec
    def add(a,b):
        pass

    ret1 = add(1,2)
    time.sleep(1)
    ret2 = add(1,2)
    
    assert ('successfully executed' in ret1 and 'can not execute' in ret2) or \
        ('successfully executed' in ret2 and 'can not execute' in ret1)


##########################################################

def test_odd_sec_2():
    
    @odd_sec
    def printme(*args):
        print(*args)

    ret1 = printme('hello', 'there')
    time.sleep(1)
    ret2 = printme('hello')
    
    assert ('successfully executed' in ret1 and 'can not execute' in ret2) or \
        ('successfully executed' in ret2 and 'can not execute' in ret1)
        

##########################################################

def test_logged():
    
    @logged
    def printme(*args):
        print(*args)

    ret1 = printme('hello', 'there')
    assert ('log:printme was executed at' in ret1)
    
    ret1 = printme()
    assert ('log:printme was executed at' in ret1)
    
    ret1 = printme()
    assert not('log:inner was executed at' in ret1)
    
    
 ##########################################################   
    

def test_timed_n():
    
    @timed_n(10)
    def printme(*args):
        print(*args)

    ret1 = printme('hello', 'there')
    ret1 = ret1.split(':')
    assert float(ret1[0]) > 0 and ret1[1] == 'printme()' and int(ret1[2]) == 10
    
 
##########################################################  
     
def test_timed_n_2():
    
    @timed_n(-1)
    def printme(*args):
        pass
    
    with pytest.raises(ValueError):
        printme('hello', 'there')
    
    


##########################################################  

def test_authenticatedOrNot_Authorized():
    global global_result
    
    @authenticatedOrNot(False)
    def printme1(*args):
        pass
    
    printme1('hello', 'there')    
    assert 'You are not authenticated' in global_result
    
    global_result.clear()
    
##########################################################  

def test_authenticatedOrNot_NotAuthorized():
    global global_result
    print('global = ', global_result)
    
    @authenticatedOrNot(True)
    def printme2(*args):
        pass
    
    printme2('hello', 'there')
    assert 'You are authenticated' in global_result
    global_result.clear()
    
##########################################################  
    
    
def test_auth_factory():   
    @auth_factory('high')
    def createfile(filename):
        print('success: created a file ', filename)
    
    def createfolder(filename):
        print('success: created a file ', filename)
    
    def editfile(filename):
        print('success: created a file ', filename)
    
    def readfile(filename):
        print('success: created a file ', filename)

   
    print(createfile('a.txt'))
  
    @auth_factory('low')
    def createfolder(filename):
        print('success: created a file ', filename)
        
    print(createfolder('a.txt'))