#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 3 ===

from Bio.Seq import Seq
from Bio.SeqUtils import GC

#Open and read the "extract_coding.txt" file
#strip() string method remove both the leading and the trailing characters (based on the string argument passed)
handle = open("extract_coding.txt","r")
txt_seq=handle.readline().strip()
handle.close()


# 5) Create a new Seq Object with the extracted sequence
my_seq = Seq(txt_seq)

# 6) print the 50th first bases of the sequence
print("Sequence:",my_seq[:50],"...")
#print the length of the sequence
print("Sequence length:",len(my_seq))

# 7) calculate (A+T)/(G+C) ratio:
nbr_A=my_seq.count("A")
nbr_T=my_seq.count("T")
nbr_G=my_seq.count("G")
nbr_C=my_seq.count("C")
AT_GC_ratio=(nbr_A+nbr_T)/(nbr_G+nbr_C)
print("AT/GC ratio: %0.02f" % AT_GC_ratio)

#calculate GC%
gc_percent=GC(my_seq)
print("GC%:",round(gc_percent,2))

# 8) Find the coding region
#find the first "ATG" from the beginning  of the sequence and store the index in a variable
coding_start=my_seq.find("ATG")

#find the first "TAG" from the end of the sequence
coding_end=my_seq.rfind("TAG")+3 #+3 to get the "TAG" codon

print("coding index: start = {} -- end = {}".format(coding_start,coding_end))
#extract the coding sequence
coding_sequence=my_seq[coding_start:coding_end]

print("Coding sequence:",coding_sequence)
print("Coding sequence length:",len(coding_sequence))

# 9) Translate coding sequence to protein
proteic_seq=coding_sequence.translate()
print("Proteic sequence:",proteic_seq)
print("Proteic sequence length:",len(proteic_seq))

# 10) pretty string showing the 6 frame translations and GC content
# https://biopython.org/docs/latest/api/Bio.SeqUtils.html => six_frame_translations()
from Bio.SeqUtils import six_frame_translations
print("\n=== Six frame translation ===\n",six_frame_translations(my_seq))
