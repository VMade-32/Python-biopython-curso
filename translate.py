import os
import sys

CODON_TABLE: dict[str, str] = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "AUG": "Met",  
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys",
    "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser",
    "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}

def validate_codon(sequence:str) -> None:
    valid_bases= set("AUGC")
    invalid = set(sequence) - valid_bases
    if invalid:
        raise ValueError(f"bases invalidas: '{''.join(invalid)}' en la secuencia: '{sequence}'")


def translate_codon(sequence: str, start_at_aug: bool = True) -> list[str]:
    sequence = sequence.upper().replace(" ", "")
    validate_codon(sequence)

    if start_at_aug:
        start_index = sequence.find("AUG")
      
    protein: list[str] = []

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon)

        if amino_acid is None:
            raise ValueError(f"Unknown codon: '{codon}' at position {i}.")

        if amino_acid == "STOP":
             break
   
        protein.append(amino_acid)

    return protein
    
if __name__ == "__main__":
    rna_sequence = (input("Ingrese la secuencia de ARN: ")).strip()
    protein = translate_codon(rna_sequence)

    print("Proteina traducida: ", " ".join(protein))
