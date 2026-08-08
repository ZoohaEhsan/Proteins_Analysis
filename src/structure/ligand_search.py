from Bio.PDB.Polypeptide import is_aa

def ligand_analysis(structure, results):
    het_atoms = []
    print("\nAvailable HETATM Residues")
    print("----------------------------------")

    for model in structure:
        for chain in model:
            for residue in chain:
                if not is_aa(residue):
                    het_atoms.append((chain.id, residue))
                    print(
                        f"{len(het_atoms)}. "
                        f"Chain {chain.id} | "
                        f"{residue.get_resname()} | "
                        f"Residue {residue.id[1]}"
                    )
    if not het_atoms:
        print("No HETATM residues found.")
        return

    choice = int(input("\nSelect HETATM residue: "))
    chain_id, ligand = het_atoms[choice - 1]
    print(
        "\nSelected:",
        f"Chain {chain_id} |",
        ligand.get_resname(),
        ligand.id[1]
    )

    print("\nAtoms in Selected Residue")
    print("----------------------------------")
    ligand_atoms = []
    for atom in ligand:
        ligand_atoms.append(atom)
        print(
            f"{len(ligand_atoms)}. "
            f"{atom.get_name()}"
        )

    # User selects atom
    atom_choice = int(input("\nSelect ligand atom: "))
    ligand_atom = ligand_atoms[atom_choice - 1]
    print("\nSelected atom:", ligand_atom.get_name())

    # Distance cutoff
    cutoff = float(input("\nEnter distance cutoff in Å: "))
    chain = structure[0][chain_id]
    print(f"\nResidues within {cutoff} Å of {atom_choice}")
    print("----------------------------------")

    nearby_residues = []
    for residue in chain:
        if "CA" in residue:
            distance = residue["CA"] - ligand_atom
            if distance < cutoff:
                result = (
                    f"{residue.get_resname()} "
                    f"{residue.id[1]} "
                    f"{distance:.2f} Å"
                )
                print(result)
                nearby_residues.append(result)

    # Store ligand selection
    results.append({
        "Analysis": "Selected Ligand",
        "Result": (
            f"Chain {chain_id} | "
            f"{ligand.get_resname()} | "
            f"Residue {ligand.id[1]}"
        )
    })

    # Store selected ligand atom
    results.append({
        "Analysis": "Selected Ligand Atom",
        "Result": ligand_atom.get_name()
    })

    # Store cutoff
    results.append({
        "Analysis": "Ligand Distance Cutoff",
        "Result": f"{cutoff} Å"
    })

    # Store nearby residues
    results.append({
        "Analysis": "Residues Near Ligand",
        "Result": " | ".join(nearby_residues)
    })