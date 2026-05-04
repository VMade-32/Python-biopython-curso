from Bio import SeqIO
from Bio.Seq import Seq
import sys
from file_finder import FilePathFinder

finder = FilePathFinder()


all_fasta = finder.find_by_extension("fasta")
print(f"DEBUG: Found FASTA files: {all_fasta}")

Wa_fasta = finder.find_first("Wa.fasta")
Wuhan_fasta = finder.find_first("Wuhan.fasta")

print(f"DEBUG: Wa_fasta path: {Wa_fasta}")
print(f"DEBUG: Wuhan_fasta path: {Wuhan_fasta}")

if Wa_fasta:
    for reg_Wa in SeqIO.parse(str(Wa_fasta), "fasta"):
        print(reg_Wa.id)
        print(reg_Wa.seq)
else:
    print("Error: Wa.fasta not found")

if Wuhan_fasta:
    for reg_Wuhan in SeqIO.parse(str(Wuhan_fasta), "fasta"):
        print(reg_Wuhan.id)
        print(reg_Wuhan.seq)
else:
    print("Error: Wuhan.fasta not found")
    
nsp1=Seq("auggagagccuugucccugguuucaacgagaaaacacacguccaacucaguuugccuguuuuacagguucgcgacgugcucguacguggcuuuggagacuccguggaggaggucuuaucagaggcacgucaacaucuuaaagauggcacuuguggcuuaguagaaguugaaaaaggcguuuugccucaacuugaacagcccuauguguucaucaaacguucggaugcucgaacugcaccucauggucauguuaugguugagcugguagcagaacucgaaggcauucaguacggucguaguggugagacacuugguguccuugucccucaugugggcgaaauaccaguggcuuaccgcaagguucuucuucguaagaacgguaauaaaggagcugguggccauaguuacggcgccgaucuaaagucauuugacuuaggcgacgagcuuggcacugauccuuaugaagauuuucaagaaaacuggaacacuaaacauagcagugguguuacccgugaacucaugcgugagcuuaacggaggg")
nsp1=nsp1.upper()
nsp1=nsp1.back_transcribe()
print(nsp1)

if nsp1 in reg_Wuhan:

   print("yes")
else:
    print("no")

if nsp1 in reg_Wa:

   print("yes")
else:
    print("no")


reg_Wa.seq.find(nsp1)

print(reg_Wuhan.seq.find(nsp1))
print("len Wa: ", len(reg_Wa.seq))
print("len Wuhan: ", len(reg_Wuhan.seq))

A= reg_Wa.count("A")
print("#A:", A)
T= reg_Wa.count("T")
print("#T:", T)
C= reg_Wa.count("C")
print("#C:", C )
G= reg_Wa.count("G")
print("#G:", G)

print("Registro Wa")
for reg_wuhan in SeqIO.parse("Wa.fasta", "fasta"):
    print("ID:", reg_Wa.id)
    print("seq:", reg_Wa.seq)

print("Registro Wuhan")
for reg_wuhan in SeqIO.parse("Wuhan.fasta", "fasta"):
    print("ID:", reg_Wuhan.id)
    print("seq:", reg_Wuhan.seq)

print(reg_Wa.seq.find(nsp1))
print(reg_Wuhan.seq.find(nsp1))

nsp9=Seq("aauaaugagcuuaguccuguugcacuacgacagaugucuugugcugccgguacuacacaaacugcuugcacugaugacaaugcguuagcuuacuacaacacaacaaagggagguagguuuguacuugcacuguuauccgauuuacaggauuugaaaugggcuagauucccuaagagugauggaacugguacuaucuauacagaacuggaaccaccuuguagguuuguuacagacacaccuaaagguccuaaagugaaguauuuauacuuuauuaaaggauuaaacaaccuaaauagagguaugguacuugguaguuuagcugccacaguacgucuacaa")
nsp9=nsp9.upper()
nsp9=nsp9.back_transcribe()
print(nsp9)
