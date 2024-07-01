#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 1 ===

#Import biopython libraries
from Bio.Seq import Seq

#DNA sequence       "ATGAAACGATGGCATTACGCTAGCATTGTTTACAATTTGACGGA"
#part to extract    "         TGGCATTACGCTAGCATTGT               "

# a) Create a new Seq object with this sequence
my_seq = Seq("ATGAAACGATGGCATTACGCTAGCATTGTTTACAATTTGACGGA")

# b) Get and print the length of the sequence
print("seq {} is {} bases long".format(my_seq, len(my_seq)))

# c) Extract the region highlighted in yellow in a new variable
#DNA sequence       "ATGAAACGATGGCATTACGCTAGCATTGTTTACAATTTGACGGA"
#part to extract    "         TGGCATTACGCTAGCATTGT               "
#                             9-------------------29
seq_region=my_seq[9:29]
print("extracted region:",seq_region)

#"TGGCATTACGCTAGCATTGT"
#   2  5  8...
# d) Extract the 3rd codon positions letters for the extracted region
print("3rd codon positions letters:",seq_region[2::3])

# e) Print the reverse sequence from the extracted region and give the 1st codon position for the reversed sequence
rev_region=seq_region[::-1]
print("reversed region:",rev_region)
#TGTTACGATCGCATTACGGT
print("1st codon letters for reversed region:",rev_region[0::3])
