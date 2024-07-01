#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 2 ===

from Bio.Seq import Seq

# create a sequence object
my_seq = Seq("CATGTAGACTAG")

# 1) Two possible ways to calculate GC%

# Manual calculation
gc_content = 100 * float(my_seq.count("G")+my_seq.count("C"))/len(my_seq)
print("Manual calculation:",gc_content)

# use Bio.SeqUtils module
from Bio.SeqUtils import GC
gc_content = GC(my_seq)
print("Bio.SeqUtils GC method:",gc_content)

# 2) You will find documentation about melting temperature calculation here:
# https://biopython.org/docs/latest/api/Bio.SeqUtils.MeltingTemp.html

from Bio.SeqUtils import MeltingTemp as mt
mt_Tm_GC = mt.Tm_GC(my_seq)
print("melting temperature Tm_GC:",mt_Tm_GC)

#=========================================================
#How to round the result to 2 digits after decimal point ?
#use the round() function: round(number, ndigits)
print("GC%:",round(gc_content,2))
print("Tm_GC:",round(mt_Tm_GC,2))
