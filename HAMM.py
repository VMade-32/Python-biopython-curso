from Bio.Seq import Seq
from Bio import SeqIO

str1=Seq("GAGCCTACTAACGGGAT")
str2=Seq("CATCGTAATGACGGCCT")
count=0

for i in range(len(str1)):
    if str1[i]!=str2[i]:
        count+=1

print(f"La distancia de Hamming es: {count}")

for seq_Wa in SeqIO.parse("Wa.fasta", "fasta"):
    print(seq_Wa.seq)
    print(len(seq_Wa.seq))
 

for seq_Wuhan in SeqIO.parse("Wuhan.fasta", "fasta"):
    print(seq_Wuhan.seq)
    print(len(seq_Wuhan.seq))
    print(len(seq_Wuhan.seq)-len(seq_Wa.seq))
    count=0

for i in range(len(seq_Wa.seq)):
    if seq_Wa.seq[i]!=seq_Wuhan.seq[i]:
        count+=1

print("la distancia de Hamming es:", count+57)
