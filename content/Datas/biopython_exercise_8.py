#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === Exercise 8 ===

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
