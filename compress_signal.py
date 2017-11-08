#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:18:20 2017

@author: oskar
"""
from huffman import *
import numpy as np
   
fname = 'Z001.txt'
with open(fname) as f:
    data = f.readlines()
data = [x.replace('\n','') for x in data]

###In time domain
v = count_unique_values(data)  
coding_tree = create_huffman_code(v)
d = tree_to_bin_dict(coding_tree)

#ocurrences dictionary sorted by the occurences of values in data
a = [[ch,v[ch]] for ch in v]
a = sorted(a, key = lambda x:x[1], reverse = True)
            
tmp = [int(ch) for ch in data]
size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data)
size_coded = sum([v[ch]*len(d[ch]) for ch in v])
    
compression_level = size_coded/size_uncoded*100
print('(TIME DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))



###In frequency domain
data_fft = list(np.abs(np.fft.fft([int(x) for x in data])))
data_fft = [str(ch) for ch in data_fft[:int(len(data_fft)/2)]]
v = count_unique_values(data_fft)  
coding_tree = create_huffman_code(v)
d = tree_to_bin_dict(coding_tree)

#ocurrences dictionary sorted by the occurences of values in data_fft
a = [[ch,v[ch]] for ch in v]
a = sorted(a, key = lambda x:x[0], reverse = True)
            
tmp = [int(float(ch)) for ch in data_fft]
size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data_fft)
size_coded = sum([v[ch]*len(d[ch]) for ch in v])
    
compression_level = size_coded/size_uncoded*100
print('(FREQUENCY DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))



###In time/frequency domain
data_spektr = list(np.abs(np.fft.fft([int(x) for x in data])))
data_fft = [str(ch) for ch in data_fft]
v = count_unique_values(data_fft)  
coding_tree = create_huffman_code(v)
d = tree_to_bin_dict(coding_tree)

#ocurrences dictionary sorted by the occurences of values in data_fft
a = [[ch,v[ch]] for ch in v]
a = sorted(a, key = lambda x:x[0], reverse = True)
            
tmp = [int(float(ch)) for ch in data_fft]
size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data_fft)
size_coded = sum([v[ch]*len(d[ch]) for ch in v])
    
compression_level = size_coded/size_uncoded*100
print('(TIME/FREQUENCY DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))
