def distance_calculator(structure, results):
    chain_id = input("Enter chain ID: ").upper()
    residue_a = int(input("Input first residue number: "))
    residue_b = int(input("Input second residue number: "))
    chain = structure[0][chain_id]

    atom1 = chain[residue_a]["CA"]
    atom2 = chain[residue_b]["CA"]
    distance = atom1 - atom2
    print(
        f"\nDistance between CA atoms: "
        f"{distance:.2f} Å"
    )

    results.append({
        "Analysis": (
            f"CA Distance - Chain {chain_id}, "
            f"Residues {residue_a} and {residue_b}"
        ),
        "Result": f"{distance:.2f} Å"
    })