def protein_translation(rna: str) -> list[str] | str:
    codon_translation = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Serine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'Stop',
        'UAG': 'Stop',
        'UGA': 'Stop',

    }
    rna = rna.upper().strip()
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]

    aminoacid_seq = []
    for codon in codons:
        if codon_translation[codon] == 'Stop':
            return 'Protein Terminated'

        aminoacid_seq.append(codon_translation[codon])

    return aminoacid_seq


print(protein_translation("AUGUUUUCU"))