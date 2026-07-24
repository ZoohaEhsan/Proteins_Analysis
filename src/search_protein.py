from Bio import Entrez
Entrez.email = '017930msbis26@iiu.edu.pk'

# Searching NCBI  for Hemoglobin Protein Ids
handle = Entrez.esearch(
    db='protein',
    term='Hemoglobin[Protein Name] AND Homo sapiens[Organism]',
)
record = Entrez.read(handle)
handle.close()
print(record)
for ID in record["IdList"]:
    print('Retrieved Id:', ID)

protein_id = record["IdList"][0]
print('Selected Protein Id:', protein_id)

# Fetching FASTA Sequence for selected Protein Id
handle = Entrez.efetch(
    db = 'protein',
    id = 109893891,
    rettype = 'fasta',
    retmode = 'text')
pro_rec = handle.read()
handle.close()
print('Retrieved Protein Record:', pro_rec)

# Saving protein FASTA sequence
with open("../../protein.fasta", "w") as file:
    file.write(pro_rec)

# Parse FASTA Using SeqIO
from Bio import SeqIO
record = SeqIO.read( "../../protein.fasta","fasta")
print('Protein Sequence:', record.seq)
print('Sequence Length:', len(record.seq))