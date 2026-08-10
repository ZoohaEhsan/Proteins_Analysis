from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

Entrez.email = "enter email"

def retrieve_gene_data():

# Gene name input and validation
    while True:
        gene = input("Enter gene symbol: ").strip().upper()
        if gene.replace("_", "").isalnum():
            break
        print("Invalid gene symbol. Please use letters and numbers only.")

# Specie name input and  validation
    while True:
        organism = input("Enter organism (e.g., Homo sapiens): ").strip()
        if all(char.isalpha() or char.isspace() for char in organism):
            break
        print("Invalid organism name. Use letters and spaces only.")


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
        return None
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
    genbank_file = f"data/{gene}.gb"
    with open(genbank_file, "w") as file:
        file.write(genbank_text)
    print("\nGenBank record saved successfully.")

    # Read GenBank Record
    dna = SeqIO.read(genbank_file, "genbank")

    # Extract Protein Information
    protein_accession = ""
    protein_name = ""
    protein_sequence = ""

    for feature in dna.features:
        if feature.type == "CDS":
            gene_name = feature.qualifiers.get("gene", [""])[0]
            if gene_name.upper() == gene.upper():
                protein_accession = feature.qualifiers.get(
                    "protein_id",
                    ["Unknown"]
                )[0]

                protein_name = feature.qualifiers.get(
                    "product",
                    ["Unknown"]
                )[0]

                protein_sequence = feature.qualifiers.get(
                    "translation",
                    [""]
                )[0]

                break

    if protein_accession == "":
        print(f"\nNo CDS found for gene '{gene}'.")
        return

    print("\nProtein Information")
    print("------------------------------")
    print("Protein Accession :", protein_accession)
    print("Protein Name :", protein_name)
    print("Protein Length :", len(protein_sequence), "aa")

    # Save Protein FASTA
    protein_record = SeqRecord(
        Seq(protein_sequence),
        id=protein_accession,
        description=protein_name
    )
    protein_file = f"data/{gene}_protein.fasta"
    SeqIO.write(protein_record, protein_file, "fasta")
    print(f"\nProtein sequence saved to '{protein_file}'.")

    # Return values for the next module
    return gene, protein_accession, protein_name, protein_file
