#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Identify ORFs ===

#Import biopython libraries
from Bio import SeqIO

#open the genbank file usinf read() method => single record
record = SeqIO.read("NC_005816.gb","genbank")

#we must use the Bacterial codon table (Nbr: 11)
transl_table = 11

#set the minimum prot sequence size to keep
min_pro_len = 100

# we want to search in each strands (+ / -)
# (+) => record.seq
# (-) => record.seq.reverse_complement()
for strand, seq in [("(+)", record.seq),("(-)", record.seq.reverse_complement())]:

    #You have 3 frame by strand: Frame 0, 1, 2  --- range(3) => [0,1,2]
    for frame in range(3):

        # with the translate() methode the sequence must be a multiple of 3
        # Euclidean division: a // b => ex: 8/3 = 2.666 -- 8//3=2
        length = 3*((len(record.seq)-frame) // 3)

        # use slicing to get the current frame
        # then translate it and split it at each stop positions
        orfs_list = seq[frame:frame+length].translate(transl_table).split("*")

        # explore the ORF list
        for pro in orfs_list:
            #if the length of the prot sequence is >= min_pro_len
            #print the ORF
            if len(pro) >= min_pro_len:
                print("%s...%s - length %i, strand %s, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
