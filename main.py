from sequence.retrieve_gene_data import retrieve_gene_data
from sequence.search_uniprot import search_uniprot
from structure.download_pdb import download_pdb
from structure.structure_reader import read_structure
from structure.structure_menu import structure_menu
import csv

results = []

# STEP 1: Collecting sequence information
result = retrieve_gene_data()
if result is not None:
    gene, protein_accession, protein_name, protein_file = result

# STEP 2: Uniprot searching
    result = search_uniprot(protein_accession)
    if result is not None:
        uniprot_id, pdb_id = result
        print("UniProt ID:", uniprot_id)
        print("Selected PDB:", pdb_id)

#Step 3: Downloading PDB file
pdb_file = download_pdb(pdb_id)
if pdb_file is None:
    print("Unable to continue because the PDB file could not be downloaded.")
    exit()

# Step 4: Read Structure
structure, title = read_structure(pdb_file)
print("\nStructure Title:")
print(title)
structure_menu(structure, results)

#Step 5: Export Results of step 4 to csv
results_file = f"{gene}_analysis_results.csv"
with open(results_file, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["Analysis", "Result"])
    writer.writeheader()
    writer.writerows(results)
    print(
            f"\nAnalysis results saved to "
            f"'{results_file}'."
        )