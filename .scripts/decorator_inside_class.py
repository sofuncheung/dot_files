# -*- coding: utf-8 -*-

'''
This is a test script to see how a decorator inside class behaves.
(When there is two 'self')
'''


def decorator_outside(method):
    '''
    So, Apparently the 'self' here stands for the class in which the
    decorator is located. 
    '''
    def method_to_decorate(self):
        print('This method is decorated outside!!!')
        print('Name is:' , self.name)
        method(self) 
    return method_to_decorate


class Fruit(object):
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.color = 'red'
        
    def get_attribute(self): # Here self is 'Fruit'
        color= self.color 
        def decorator_inside(method):
            def method_to_decorate(self):
                print('This method is decorated inside!!!')
                print('Color is:' , color)
                method(self)
            return method_to_decorate
        return decorator_inside
            
    #@decorator_outside
    @get_attribute(self)
    def print_price(self):
        print('Price is:', self.price)
        


if __name__ == '__main__':
    x = Fruit('Apple', 10)
    x.print_price()