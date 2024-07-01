#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 4 ===

# parse the « srk_alleles.fasta » file and return for each record: sequence id, sequence length, GC%
#=== with optional question ===
from Bio import SeqIO
from Bio.SeqUtils import GC

print("=== with optional question ===")
records = SeqIO.parse("../srk_alleles.fasta","fasta")

#List to store length and GC%
len_list=[]
gc_list=[]

for rec in records:
    seq_len = len(rec.seq)
    seq_GC = GC(rec.seq)

    #Append a new value in a list
    len_list.append(seq_len)
    gc_list.append(seq_GC)

    print("Seq ID: {sId} -- Seq length: {sLen} bp -- GC%: {gcP}".format(sId=rec.id,sLen=seq_len,gcP=seq_GC))

#mean calculation
mean_len = sum(len_list)/len(len_list)
mean_GC = sum(gc_list)/len(gc_list)

#min() return the minimum value of a numeric list. max() return the maximum value.
print("mean length: {} (min: {} max: {})-- mean GC%: {}".format(mean_len,min(len_list),max(len_list),mean_GC))
