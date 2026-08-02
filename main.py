from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

Entrez.email = ""

# Taking Input from User
gene = input("Enter gene symbol: ")
organism = input("Enter organism (e.g., Homo sapiens): ")
max_results = input("Enter the number of records to retrieve (Press Enter for 5): ")

if max_results == "":
    max_results = 5
else:
    max_results = int(max_results)

query = f"{gene}[Gene] AND {organism}[Organism]"

# Search NCBI
handle = Entrez.esearch(
    db="nucleotide",
    term=query,
    retmax=max_results
)
record = Entrez.read(handle)
handle.close()

print("Total Matching Records:", record["Count"])
print("Retrieved Records:", len(record["IdList"]))

if not record["IdList"]:
    print("No records found.")
    exit()

ids = record["IdList"]
print("\nAvailable Records:\n")

for i, nucleotide_id in enumerate(ids, start=1):
    handle = Entrez.efetch(
        db="nucleotide",
        id=nucleotide_id,
        rettype="fasta",
        retmode="text"
    )
    fasta = handle.read()
    handle.close()

    header = fasta.split("\n")[0]
    print(f"{i}. {header}")

# User selects a record
choice = int(input("\nSelect a record number: "))
selected_id = ids[choice - 1]

print("\nSelected Nucleotide ID:", selected_id)

# Retrieve GenBank Record
handle = Entrez.efetch(
    db="nucleotide",
    id=selected_id,
    rettype="gb",
    retmode="text"
)

genbank_text = handle.read()
handle.close()

# Save GenBank Record
genbank_file = f"{gene}.gb"
with open(genbank_file, "w") as file:
    file.write(genbank_text)
print("\nGenBank record saved successfully.")

# Read GenBank Record
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

# Protein Information
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
