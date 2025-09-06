# Extensible Stack
# Basically a stack but works by pre-allocating space.
# When we overflow the stack we allocate to a new length
# and copy the old contents over.

from __future__ import annotations
from typing import List
import json

# The Extensible Stack class.
# DO NOT MODIFY!
class EStack():
    def  __init__(self,
                  m : int,
                  b : int):
        self.m               = m
        self.b               = b
        self.allocatedlength = 1
        self.currentpointer  = 0
        self.data            = [None]

    # DO NOT MODIFY!
    def esdump(self) -> str:
        return json.dumps(self.data)

    # Push an integer onto the stack.
    # This should put something at index currentpointer.
    # If we overflow the stack then create a new stack
    # of length m * stacklength + b.
    # Copy the data over and then push.

    def espush(self,x:int):
        if self.currentpointer == self.allocatedlength:
            newStackLength = self.m * self.allocatedlength + self.b
            newdata = [None] * newStackLength

            for i in range(self.allocatedlength):
                newdata[i] = self.data[i]
            self.data = newdata
            self.allocatedlength = newStackLength
            
        self.data[self.currentpointer] = x
        self.currentpointer += 1
            
    # Pop an integer off the stack quietly,
    # meaning just do it and don't return anything.

    def espop_quiet(self):
        self.data[self.currentpointer - 1] = None
        self.currentpointer -= 1

    # Pop an integer off the stack and return it.

    def espop(self):
        r = self.data[self.currentpointer - 1]
        self.data[self.currentpointer - 1] = None
        self.currentpointer -= 1
        return r