from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa

# ---------------- Read Structure ----------------
def read_structure(pdb_file):
    title = ""
    with open(pdb_file, "r") as file:
        for line in file:
            if line.startswith("TITLE"):
                title += line[10:].strip() + " "
            elif line.startswith("ATOM"):
                break

    title = title.strip()
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(title, pdb_file)
    return structure, title


# ---------------- Chains ----------------
# Displaying Chains
def list_chains(structure, results):
    chains = []
    model = structure[0]
    for chain in model:
            print(f"Chain {chain.id}")
            chains.append(chain.id)
    results.append({
        "Analysis": "Chains",
        "Result": ", ".join(chains)
    })

# Count chains
def count_chains(structure, results):
    count = 0
    for chain in structure[0]:
        count += 1
    print("Total Chains:", count)
    results.append({
        "Analysis": "Total Chains",
        "Result": count
    })

# ---------------- Residues ----------------
# Display Residues
def list_residues(structure, results):
    residues = []
    for model in structure:
        for chain in model:
            for residue in chain:
                result = (
                    f"Chain {chain.id}: "
                    f"{residue.get_resname()} "
                    f"{residue.id[1]}"
                )
                print(result)
                residues.append(result)
    results.append({
        "Analysis": "Residues",
        "Result": " | ".join(residues)
    })

# Count Residues
def count_residues(structure, results):
    count = 0
    for model in structure:
        for chain in model:
            for residue in chain:
                count += 1
    print("Total Residues:", count)
    results.append({
        "Analysis": "Total Residues",
        "Result": count
    })

# First 10 Residues
def first_ten_residues(structure, results, chain_id="A"):
    chain = structure[0][chain_id]
    residues = []
    count = 0
    for residue in chain:
        result = f"{residue.get_resname()} {residue.id[1]}"
        print(result)
        residues.append(result)
        count += 1
        if count == 10:
            break

    results.append({
        "Analysis": f"First 10 Residues - Chain {chain_id}",
        "Result": ", ".join(residues)
    })

# Last Amino Acid
def last_amino_acid(structure, results):
    last_results = []
    for model in structure:
        for chain in model:
            amino_acids = []
            for residue in chain:
                if is_aa(residue):
                    amino_acids.append(residue)
            if amino_acids:
                last = amino_acids[-1]
                result = (
                    f"Chain {chain.id}: "
                    f"{last.get_resname()} "
                    f"{last.id[1]}"
                )
                print(result)
                last_results.append(result)

    results.append({
        "Analysis": "Last Amino Acid",
        "Result": " | ".join(last_results)
    })


# ---------------- Atoms ----------------

def list_atoms_in_residue(
    structure,
    results,
    chain_id,
    residue_number
):
    chain = structure[0][chain_id]
    residue = chain[residue_number]
    print(
        f"\nAtoms in Residue {residue_number} "
        f"(Chain {chain_id})"
    )
    print("----------------------------------")
    atoms = []
    for atom in residue:
        atom_name = atom.get_name()
        print(atom_name)
        atoms.append(atom_name)

    results.append({
        "Analysis": (
            f"Atoms - Chain {chain_id}, "
            f"Residue {residue_number}"
        ),
        "Result": ", ".join(atoms)
    })