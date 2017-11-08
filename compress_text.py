#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:15:59 2017

@author: oskar
"""

from huffman import *
import numpy as np
   
fname = 'Text_data.txt'
with open(fname) as f:
    data = f.read().lower()
data = [x for x in data if x!= '\n']

v = count_unique_values(data)  
coding_tree = create_huffman_code(v)
d = tree_to_bin_dict(coding_tree)

#ocurrences dictionary sorted by the occurences of values in data
a = [[ch,v[ch]] for ch in v]
a = sorted(a, key = lambda x:x[1], reverse = False)
            
size_uncoded = 8*len(data)
size_coded = sum([v[ch]*len(d[ch]) for ch in v])
    
compression_level = size_coded/size_uncoded*100
print('Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))


