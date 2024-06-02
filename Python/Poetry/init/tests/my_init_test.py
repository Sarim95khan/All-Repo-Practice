from init import main

def test_function1():
     r= main.my_function(3)
     assert r == 4

def test_function2():
     r= main.my_function(2)
     assert r== 3