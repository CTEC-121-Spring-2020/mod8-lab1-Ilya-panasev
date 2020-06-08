"""
CTEC 121
Ilya Panasevich
Module 8 Lab 1
class demos
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
from dog import Dog
from msdie import MSDie
import docTest

def main():
    '''
    print()
    print(5*'All That')
    print()
    '''
    # section 1
    '''
    win = GraphWin("demo", 1000, 1000)
    myCircle = Circle(Point(500, 500), 200)
    myCircle.setFill("green")
    myCircle.draw(win)
    win.getMouse()
    '''
    # section 2
    '''
    d = Dog("dog")
    print(d)
    print(d.getName())
    d.setName("Godzilla")
    print(d.getName())

    d.bark()
    '''
    # section 3
    """
    die = MSDie(6)
    print("number of sides", die.getSides())
    print("value:", die.getValue())
    die.setValue(5)
    print("value:", die.getValue())
    die.setValue(12)
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    """
    print()
    # print module file/file header documentation 
    print(docTest.__doc__)
    # print class docs
    print(docTest.DocTest.__doc__)
    # print method docs
    print(docTest.DocTest.method.__doc__)
    print()

main()    