# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:51:08 2017

@author: Oskar
"""

class Node:
    def __init__(self,val,name, l=None, r=None):
        self.value = val
        self.name = str(name)
        self.children = [l,r]
       
TMP = 1
def count_unique_values(v):
    tmp = {}
    for x in set(v):
        tmp[x]=v.count(x)
    return tmp

def create_huffman_code(v):
    #initial list of trees
    trees = []
    for x in v:
        trees.append(Node(v[x],x))
        
    trees.sort(key=lambda x:x.value)
    while len(trees)>1:
        trees[0]=Node(val=(trees[0].value+trees[1].value),name=trees[0].name+';'+trees[1].name, l=trees[0], r=trees[1])
        del trees[1]
        trees.sort(key=lambda x:x.value)
    return trees[0]
            
def tree_to_bin_dict(coding_tree, x={}):
    global TMP 
    TMP += 1
    if coding_tree.children[0]:
        tmp = coding_tree.children[0].name.split(';') 
        for ch in tmp:
            if not ch in x.keys():
                x[ch] = '0'
            else:
                x[ch] += '0'
        x = tree_to_bin_dict(coding_tree.children[0],x)
    if coding_tree.children[1]:
        tmp = coding_tree.children[1].name.split(';')  
        for ch in tmp:
            if not ch in x.keys():
                x[ch] = '1'
            else:
                x[ch] += '1'
        x = tree_to_bin_dict(coding_tree.children[1],x)
    return x

 