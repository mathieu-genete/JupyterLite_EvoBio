#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 5 ===

from Bio import SeqIO

#Write the fasta file function
def write_fasta(filename,record):
    #Print fasta file using SeqIO write function
    SeqIO.write(rec,filename,"fasta")

    '''
    #Using with statement
    with open(filename,"w") as fasta:
     fasta.write(record.format("fasta"))

    fasta = open(filename,"w")
    fasta.write(record.format("fasta"))
    fasta.close()
    '''
    
# Using SeqIO.parse
print("=== SeqIO.parse method ===")
records = SeqIO.parse("SPIRAL.gb","genbank")

for rec in records:
    if rec.id == 'NM_105590.3':
        print("Sequence ID :",rec.id)
        print("Seq head :",rec.seq)
        print("Sequence length :",len(rec))
        print("Organism :",rec.annotations['organism'])
        print("sequence_version :",rec.annotations['sequence_version'])
        print("molecule_type :",rec.annotations['molecule_type'])
        write_fasta("blast_NM_105590.3_FOR.fasta",rec)

# Using SeqIO.index
print("=== SeqIO.index method ===")

record_dict = SeqIO.index("SPIRAL.gb","genbank")
rec=record_dict['NM_105590.3']
print("Sequence ID :",rec.id)
print("Seq head :",rec.seq)
print("Sequence length :",len(rec))
print("Organism :",rec.annotations['organism'])
print("sequence_version :",rec.annotations['sequence_version'])
print("molecule_type :",rec.annotations['molecule_type'])
write_fasta("blast_NM_105590.3.fasta",rec)

