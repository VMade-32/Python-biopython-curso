from Bio.Seq import Seq

ADN= "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
ADN1= Seq(ADN)

print(type(ADN))
print(type(ADN.count("A")), " ", ADN.count("C"), " ", ADN.count("G"), " ", ADN.count("T"))

longitud=len(ADN)
print(longitud)
