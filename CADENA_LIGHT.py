import random as rn

bases = ["A", "T", "C", "G"]

DNA = int(input("Ingrese la longitud de ADN: "))
tripletes = []
for _ in range(DNA):
    secuencia = ""
    for i in range(3):
        secuencia += rn.choice(bases)
    print(secuencia)
    tripletes.append(secuencia)

secuencia_total = ''.join(tripletes)
print("Secuencia completa:", secuencia_total)

A= secuencia_total.count("A")
print("#A:", A)
T= secuencia_total.count("T")
print("#T:", T)
C= secuencia_total.count("C")
print("#C:", C )
G= secuencia_total.count("G")
print("#G:", G)
