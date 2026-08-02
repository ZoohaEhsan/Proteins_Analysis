from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna = SeqIO.read(genbank_file, "genbank")

print("\nNucleotide Information")
print("------------------------------")
print("Accession :", dna.id)
print("Description :", dna.description)
print("Organism :", dna.annotations["organism"])
print("Length :", len(dna.seq), "bp")

# Extract Protein Information
protein_accession = ""
protein_name = ""
protein_sequence = ""

for feature in dna.features:
    if feature.type == "CDS":
        protein_accession = feature.qualifiers.get("protein_id", ["Unknown"])[0]
        protein_name = feature.qualifiers.get("product", ["Unknown"])[0]
        protein_sequence = feature.qualifiers.get("translation", [""])[0]
        break

print("\nProtein Information")
print("------------------------------")
print("Protein Accession :", protein_accession)
print("Protein Name :", protein_name)
print("Protein Length :", len(protein_sequence), "aa")
print("First 100 Amino Acids:")
print(protein_sequence[:100])

# Save Protein FASTA
protein_record = SeqRecord(
    Seq(protein_sequence),
    id=protein_accession,
    description=protein_name
)

protein_file = f"{gene}_protein.fasta"
SeqIO.write(protein_record, protein_file, "fasta")
print(f"\nProtein sequence saved to '{protein_file}'.")