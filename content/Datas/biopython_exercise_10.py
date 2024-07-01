#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 10 ===

import os
import sys
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML

#sys.argv = list of argument of your command line sys.argv[0] is the py script filename
blast_folder=sys.argv[1] #Get blast folder from command line

#define variables
fasta_file = os.path.join(blast_folder,"srk_alleles.fasta")
unknow_fasta = os.path.join(blast_folder,"unknow_seq.fasta")
xml_results = os.path.join(blast_folder,"local_blast_results.xml")

#makeblastdb command line generation
cline=NcbimakeblastdbCommandline(dbtype="nucl",input_file=fasta_file)

#execute command line
os.system(str(cline))

#blastn command line generation
cmd = NcbiblastnCommandline(cmd='blastn', query = unknow_fasta,\
db = fasta_file, evalue = 0.01, outfmt = 5, out = xml_results, word_size=5)
print(cmd)

#execute blastn command line
os.system(str(cmd))


#Parse the BLAST results
blast_record_list=NCBIXML.parse(open(xml_results,"r"))

#Multiple queries => for statement to explore recursively each query
for blast_record in blast_record_list:
    #BLAST report for the query
    print("=== BLAST Submission report ===\n\tProgram: {b_prog}\n\tversion: {b_ver} \
\n\tDatabase: {b_db}\n\tQuery ID: {q_id}\n\tQuery description: {q_desc} \
\n\tQuery length: {q_len}".format(b_prog=blast_record.application, \
b_ver=blast_record.version,b_db=blast_record.database, \
q_id=blast_record.query_id,q_desc=blast_record.query, \
q_len=blast_record.query_length))

    #Explore Description list
    # 1) How many sequences producing significant alignments are returned ?
    print("\t=== Descriptions list ===")
    print("\tNumber of sequence producing significant alignments: {}".format(len(blast_record.descriptions)))

    for desc in blast_record.descriptions:
        print("\t{seq_align}\t{score}\t{evalue}".format(seq_align=desc.title \
,score=desc.score,evalue=desc.e))

    for alignment in blast_record.alignments:
        print("\n\t****Alignment****")
        print("\tsequence:", alignment.title)
        print("\tlength:", alignment.length)
        for hsp in alignment.hsps:
            print("\te value:", hsp.expect)
            print("\t"+hsp.query[0:75] + "...")
            print("\t"+hsp.match[0:75] + "...")
            print("\t"+hsp.sbjct[0:75] + "...")
