def coordinate_calculator(structure, results):
    chain_id = input("Enter chain ID: ").upper()
    residue_number = int(
        input("Enter residue number: ")
    )
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
    ca = residue["CA"]
    print("\nCA Coordinates:")
    print(ca.coord)

    results.append({
        "Analysis": (
            f"CA Coordinates - "
            f"Chain {chain_id}, "
            f"Residue {residue_number}"
        ),
        "Result": str(ca.coord)
    })