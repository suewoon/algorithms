#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:04:10 2017

@author: suewoonryu

binary search tree implementation in python
"""

class Node : 
    def __init__(self, val):
        self.value = val 
        self.left = None 
        self.right = None
    
    def __str__(self):
        return str(self.value)
    
    def insert(self, data):
        if self.value == data : 
            return False 
        
        elif self.value > data : 
            if self.left : 
                return self.left.insert(data)
            else : 
                self.left = Node(data)
                return self.left 
        else : 
            if self.right : 
                return self.right.insert(data)
            else : 
                self.right = Node(data)
                return self.right 
    
    def find(self, data):
        if self.value == data : 
            return True 
        
        elif self.value > data : 
            if self.left : 
                return self.left.find(data)
            else : 
                return False 
        else : 
            if self.right :
                return self.right.find(data)
            else :
                return False 
    
        
class Tree : 
    
    def __init__(self):
        self.root = None 
    
    def insert(self, data):
        if self.root : 
            return self.root.insert(data)
        else : 
            self.root = Node(data)
            return self.root 
        
    def find(self, data):
        if self.root : 
            return self.root.find(data)
        else : 
            return False 
    
    def preOrderTraversal(self):
        self._preOrderTraversal(self.root)
    def _preOrderTraversal(self, node):
        if node is not None :
            print(node, end=' ')
            self._preOrderTraversal(node.left)
            self._preOrderTraversal(node.right)
    
    def findMin(self,node):
       while node.left is not None : 
           node = node.left 
       return node
   
    def remove(self, node, data):
        if self.root is None : 
            return False 
        
        elif data < node.value :
            node.left = self.remove(node.left, data)
            
        elif data > node.value : 
            node.right = self.remove(node.right, data)
        
        else : 
            #case 1 : no child 
            if node.left== None and node.right == None : 
                del node
                node = None 
            
            #case 2 : one child 
            elif node.left == None : 
                temp = node 
                node = node.right 
                del temp 
            
            elif node.right == None :
                temp = node
                node = node.left 
                del temp
            
            #case 3 : 2 children
            else  : 
                temp = self.findMin(node.right)
                node.value = temp.value 
                node.right = self.remove(node.right, temp.value)
            
        
        return node 

bst = Tree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.remove(bst.root,10)