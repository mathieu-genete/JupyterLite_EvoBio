#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 9 ===

from Bio.Blast import NCBIXML

#parse the blast results : Single query => .read() method
blast_record=NCBIXML.read(open("BE037100_blast_results.xml","r"))

print("BLAST Submission report")
print("Program:",blast_record.application)
print("version:",blast_record.version)
print("Database:",blast_record.database)
print("Query ID:",blast_record.query_id)
print("Query description:",blast_record.query)
print("Query length:",blast_record.query_length)

#Explore Description list
# 1) How many sequences producing significant alignments are returned ?
print("=== Descriptions list ===")
print("Number of sequence producing significant alignments: {}" \
.format(len(blast_record.descriptions)))


# 2) List the 10 first sequences (sorted by e-value) and print the list as formatted as below
#The sorted() funtion is not mandatory, e-value are already sorted
# sort by e-value:
# => sort_blast_description=sorted(blast_record.descriptions,key=lambda x: x.e)
#for reverse sort:
# => sorted(blast_record.descriptions,key=lambda x: x.e, reverse=True)

print("\nSequences producing significant alignments\tScore\te-value")

#blast_record.descriptions[:10] => [:10] first 10 values of sort_blast_description list
for desc in blast_record.descriptions[:10]:
    print("{seq_align}\t{score}\t{evalue}".format(seq_align=desc.title \
,score=desc.score,evalue=desc.e))
