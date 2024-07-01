#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 4 ===

# parse the « srk_alleles.fasta » file and return for each record: sequence id, sequence length, GC%
from Bio import SeqIO
from Bio.SeqUtils import GC

# c) parse the « single_srk_allele.fasta » file and return for the record : sequence id, sequence length, GC %
print("=== « single_srk_allele.fasta » Using SeqIO.read() ===")
rec = SeqIO.read("single_srk_allele.fasta","fasta")
seq_len = len(rec.seq)
seq_GC = GC(rec.seq)
print("Seq ID: {sId} -- Seq length: {sLen} bp -- GC%: {gcP}".format(sId=rec.id,sLen=seq_len,gcP=seq_GC))

# d) parse the « srk_alleles.fasta » file and return for each record : sequence id, sequence length, GC %
print("\n=== « srk_alleles.fasta » Using SeqIO.parse() ===")
records = SeqIO.parse("srk_alleles.fasta","fasta")

for rec in records:
    seq_len = len(rec.seq)
    seq_GC = GC(rec.seq)
    print("Seq ID: {sId} -- Seq length: {sLen} bp -- GC%: {gcP}".format(sId=rec.id,sLen=seq_len,gcP=seq_GC))

# An other way to extract the sequences:
print("\n=== « srk_alleles.fasta » Using SeqIO.index() ===")
record_dict = SeqIO.index("srk_alleles.fasta","fasta")

print("Sequences ID:",",".join(record_dict.keys()))
for seq_id,rec in record_dict.items():
    seq_len = len(rec.seq)
    seq_GC = GC(rec.seq)
    print("Seq ID: {sId} -- Seq length: {sLen} bp -- GC%: {gcP}".format(sId=rec.id,sLen=seq_len,gcP=seq_GC))
