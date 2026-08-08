import requests

# Retrieve metadata for a PDB structure
def get_pdb_metadata(pdb_id):
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Unknown", "Unknown"
    data = response.json()

    # Structure Title
    title = data.get("struct", {}).get("title", "Unknown")

    # Source Organism
    organism = "Unknown"

    if "rcsb_entity_source_organism" in data:
        organism = data["rcsb_entity_source_organism"][0].get(
            "scientific_name",
            "Unknown"
        )
    return title, organism

# Searching Uniprot
def search_uniprot(protein_accession):
    print("\nSearching UniProt...")

    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={protein_accession}"
        "&format=json"
    )

    response = requests.get(url)
    if response.status_code != 200:
        print("Unable to connect to UniProt.")
        return None

    data = response.json()
    if len(data["results"]) == 0:
        print("No UniProt record found.")
        return None

    # First matching entry
    entry = data["results"][0]

    # UniProt Information
    uniprot_id = entry["primaryAccession"]
    protein_name = (
        entry["proteinDescription"]
        ["recommendedName"]
        ["fullName"]
        ["value"]
    )

    organism = entry["organism"]["scientificName"]
    print("\nUniProt Information")
    print("------------------------------")
    print("UniProt ID :", uniprot_id)
    print("Protein :", protein_name)
    print("Organism :", organism)

    # Retrieve PDB Structures
    pdb_entries = []
    for ref in entry["uniProtKBCrossReferences"]:
        if ref["database"] == "PDB":
            if len(pdb_entries) == 10:
                break

            pdb_id = ref["id"]
            title, organism = get_pdb_metadata(pdb_id)
            method = "Unknown"
            resolution = "Unknown"
            if "properties" in ref:
                for item in ref["properties"]:
                    if item["key"] == "Method":
                        method = item["value"]
                    elif item["key"] == "Resolution":
                        resolution = item["value"]

            pdb_entries.append({
                "PDB_ID": pdb_id,
                "Title": title,
                "Organism": organism,
                "Method": method,
                "Resolution": resolution
            })

    print("\nAvailable PDB Structures")
    print("------------------------------")

    if not pdb_entries:
        print("No PDB structures found.")
        return None

    for i, pdb in enumerate(pdb_entries, start=1):
        print(f"{i}.")
        print("PDB ID      :", pdb["PDB_ID"])
        print("Title       :", pdb["Title"])
        print("Organism    :", pdb["Organism"])
        print("Method      :", pdb["Method"])
        print("Resolution  :", pdb["Resolution"])
        print()

    choice = int(input("Select a PDB structure: "))

    selected_pdb = pdb_entries[choice - 1]["PDB_ID"]

    print("\nSelected PDB structure:", selected_pdb)
    print("Ready for PDB download.")

    return uniprot_id, selected_pdb