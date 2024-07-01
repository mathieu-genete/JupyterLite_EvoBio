#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 6 ===

# From NCBI nucleotide:
# accession number for "Selenipedium aequinoctiale maturase K" : EU490707

from Bio import SeqIO
from Bio import Entrez

Entrez.email="mathieu.genete@univ-lille.fr"

handle = Entrez.efetch(db = "nucleotide",id = "EU490707",rettype = "gb", retmode = "text")
record = SeqIO.read(handle,"genbank")

print("record id: {rec_id}\nsequence version : {seq_ver}\ndescription: {desc}\norganism: {orga}".format( \
rec_id = record.id, seq_ver = record.annotations['sequence_version'], desc = record.description, \
orga = record.annotations['organism'] ))

with open("EU490707.fa","w") as out_fasta:
	out_fasta.write(record.format("fasta"))
