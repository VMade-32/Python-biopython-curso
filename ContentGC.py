from Bio import SeqIO
import sys
import os

Wa_fasta="C:\\Users\\Made\\Downloads\\Wa.fasta"

for regwa in SeqIO.parse(Wa_fasta, "fasta"):
   print(regwa.id, regwa.seq)

leng=len(regwa.seq)
print(leng)

C= regwa.seq.count("C")
G= regwa.seq.count("G")
print(C, G)
print("GC content: ", (C+G)/leng*100, "%")
