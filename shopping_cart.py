
import math
import os
import random
import re
import sys

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    pass


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def get_items(self): 
        return [item.name for item in self.items]

    def get_items_count(self):
        return len(self.items)
       
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart.items)) + "\n")
        elif command == "total":
            fptr.write(str(cart.get_total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
