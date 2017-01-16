# coding:utf-8
'''
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/toy-factory
@Language: Python
@Datetime: 17-01-16 09:26
'''

"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print 'Wow'


class Cat(Toy):
    # Write your code here
    def talk(self):
        print 'Meow'


class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        # Write your code here
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()
        else:
            return Toy()