# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(5,6,3),'Scalene','5,6,3 should be scalene')

    def testNotATriangles(self): 
        self.assertEqual(classifyTriangle(6,2,1),'NotATriangle','6,2,1 should be equilateral')
        
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(620,23,1),'InvalidInput','620,23,1 is invalid input')
    
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-3,2,-1),'InvalidInput','-3,2,-1 is invalid input')
        
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle("x",23,1),'InvalidInput','"x",23,1 is invalid input')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

