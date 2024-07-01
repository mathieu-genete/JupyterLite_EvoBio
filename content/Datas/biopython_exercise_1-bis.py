#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 1-bis ===

#Import python libraries
from Bio.Seq import Seq

#DNA sequence       "ATGAAACGATGGCATTACGCTAGCATTGTTTACAATTTGACGGA"
#part to extract    "         TGGCATTACGCTAGCATTGT               "
#                             9                   29

my_seq = Seq("ATGAAACGATGGCATTACGCTAGCATTGTTTACAATTTGACGGA")
seq_region=my_seq[9:29]

# a) Check if the highlighted sub-sequence starts with TGG and ends with TAG.
print("Does extracted region starts with TGG:",seq_region.startswith("TGG"))
print("Does extracted region ends with TAG:",seq_region.endswith("TAG"))

#Other way by using start and end position
print("Does extracted region starts with TGG:",my_seq.startswith("TGG",9))
print("Does extracted region ends with TGG:",my_seq.endswith("TAG",0,29))


#b) Give the number of occurrences of “TT”. Use overlapping count and non overlapping.
print("Count 'TT' non overlapping:",my_seq.count("TT"))
print("Count 'TT' overlapping:",my_seq.count_overlap("TT"))

#=> The number of TT overlaps is greater than that of non-overlap, depending on the 2 'TTT' sub-sequences

# c) Find the first and the last occurrence of “TA”
print("first occurrence of 'TA'",my_seq.find("TA"))
print("last occurrence of 'TA'",my_seq.rfind("TA"))

# d) Find the “TCT” codon in the sequence
find_pos = my_seq.find("TCT")
if find_pos<0:
    print("'TCT' codon not found in the sequence")
else:
    print("find 'TCT' codon in the sequence at position:",find_pos)

# results = -1 ==> the 'TCT' substring not found in the sequence string.
