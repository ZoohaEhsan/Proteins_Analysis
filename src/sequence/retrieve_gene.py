from Bio import Entrez
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

Entrez.email = "017930msbis26@iiu.edu.pk"

# Search NCBI Nucleotide for HBB RefSeq mRNA
handle = Entrez.esearch(
    db="nucleotide",
    term='HBB[Gene] AND Homo sapiens[Organism] AND biomol_mrna[PROP] AND srcdb_refseq[PROP]',
    retmax=1
)

record = Entrez.read(handle)
handle.close()

print(record)

# Retrieve the first nucleotide ID
nucleotide_id = record["IdList"][0]
print("Selected Nucleotide ID:", nucleotide_id)

# Fetch the nucleotide FASTA sequence
handle = Entrez.efetch(
    db="nucleotide",
    id=nucleotide_id,
    rettype="fasta",
    retmode="text"
)

dna_record = handle.read()
handle.close()

print(dna_record)

# Save nucleotide FASTA
with open("hbb_mrna.fasta", "w") as file:
    file.write(dna_record)

print("Nucleotide sequence saved successfully.")

# Read nucleotide FASTA using SeqIO
dna = SeqIO.read("hbb_mrna.fasta", "fasta")

print("Sequence ID:", dna.id)
print("Description:", dna.description)
print("DNA Length:", len(dna.seq))

# Translate DNA into protein
protein_seq = dna.seq.translate()

print("\nTranslated Protein Sequence:")
print(protein_seq)
print("Protein Length:", len(protein_seq))

# Save translated protein as FASTA
protein_record = SeqRecord(
    protein_seq,
    id="HBB_translated",
    description="Translated protein sequence from HBB mRNA"
)

SeqIO.write(protein_record, "translated_hbb.fasta", "fasta")

print("Translated protein saved to translated_hbb.fasta")