#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 7 ===

from Bio import SeqIO
from Bio import Entrez

Entrez.email="mathieu.genete@univ-lille.fr"

#Search GRF3: Arabidopsis thaliana general regulatory factor 3 in NCBI GenBank nucleotide database
handle = Entrez.esearch(db="nucleotide",term="GRF3[Gene Name] AND Arabidopsis thaliana[Organism] ", rettype="gb", retmode="text", retmax=5)
results = Entrez.read(handle)

# a) Print how many results are returned ?
print("{rslt_count} results found".format(rslt_count=results['Count']))

# b) Use Entrez.efetch() to retrieves all records.  (Entrez.efetch() id parameter accept Python list,
# use SeqIO.parse() to parse Entrez.efetch() return value => multiple queries)
handle = Entrez.efetch(db="nucleotide",id=results['IdList'],rettype = "gb", retmode = "text")
all_records=SeqIO.parse(handle,"genbank")

print("print mRNA molecule type only:")
# e) Finally, extract those mRNA sequences in a new fasta file "GRF3_mRNA.fasta"
with open("GRF3_mRNA.fasta","w") as out_fasta:
    for record in all_records:

        # c) Recover only mRNA sequences (‘molecule_type’ annotation should be ‘mRNA’)
        if record.annotations['molecule_type']=='mRNA':

            # d) Print the record id, the sequence version, the sequence length, the description and the organism
            print("record id: {rec_id}\n\tsequence version: {seq_ver}\n\tsequence length: {seq_len}\n\tdescription: {desc}\n\t\
organism: {orga}".format(rec_id = record.id, seq_ver = record.annotations['sequence_version'], seq_len = len(record.seq) \
,desc = record.description,orga = record.annotations['organism'] ))

            # e) Finally, extract those mRNA sequences in a new fasta file "GRF3_mRNA.fasta"
            out_fasta.write(record.format("fasta"))
