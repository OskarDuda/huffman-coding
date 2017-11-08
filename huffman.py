# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:51:08 2017

@author: Oskar
"""

class Node:
    def __init__(self,val,name, l=None, r=None):
        self.value = val
        self.name = name
        self.children = [l,r]

#def find_min_tree(list_of_trees, k, return_index=True):
#    min_trees = sorted(list_of_trees[:k], key = lambda x: x.value)
#    for tree1 in list_of_trees[k:]:
#        for tree2 in min_trees:
#            if tree1.value < tree2.value:
#                tree1 = tree2             
#            
#    if return_index:
#        tree_indeces = []
#        for tree in range(k):
#            tree_indeces = list_of_trees.index(min_tree[k])
#        return [min_trees, tree_indeces]
#    else:
#        return min_tree
        

def create_huffman_code(v):
    v_values = list(v.values())
    v_keys = list(v.keys())
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
    for ch in coding_tree.children[0].name.split():
        if not x[ch]:
            x[ch] = '0'
        else:
            x[ch] += '0'
        x = tree_to_bin_dict(coding_tree.children[0],x)
    for ch in coding_tree.children[0].name.split():
        if not x[ch]:
            x[ch] = '1'
        else:
            x[ch] += '1'
        x = tree_to_bin_dict(coding_tree.children[1],x)
    return x
        
v = {'g':2, 'b':2, 'f':3, 'd':5, 'c':7, 'e':19, 'a':27}   
coding_tree = create_huffman_code(v)
d = tree_to_bin_dict(coding_tree)
            
        
code = {cipher_data(coding_tree,x,v) for x in v }

