from structure.structure_reader import (
    list_chains,
    count_chains,
    list_residues,
    count_residues,
    first_ten_residues,
    last_amino_acid,
    list_atoms_in_residue,
)

from structure.coordinates_calculator import coordinate_calculator
from structure.distance_calculator import distance_calculator
from structure.ligand_search import ligand_analysis


def structure_menu(structure, results):
    while True:
        print("""
===================================
       STRUCTURE ANALYSIS MENU
===================================

1. Display Chains
2. Count Chains
3. Display Residues
4. Count Residues
5. Display First 10 Residues
6. Display Last Amino Acid
7. Display Atoms in a Residue
8. Get CA Coordinates
9. Calculate Distance Between Residues
10. Ligand Analysis
11. Exit
""")

        choice = input("Choose an option: ")

        # Display Chains
        if choice == "1":
            list_chains(structure, results)

        # Count Chains
        elif choice == "2":
            count_chains(structure, results)

        # Display Residues
        elif choice == "3":
            list_residues(structure, results)

        # Count Residues
        elif choice == "4":
            count_residues(structure, results)

        # First 10 Residues
        elif choice == "5":
            chain = input("Enter Chain ID: ").upper()
            first_ten_residues(structure, results,chain)

        # Last Amino Acid
        elif choice == "6":
            last_amino_acid(structure,results)

        # Atoms in a Residue
        elif choice == "7":
            chain = input("Enter Chain ID: ").upper()
            residue = int(input("Enter Residue Number: "))
            list_atoms_in_residue(
                structure,
                results,
                chain,
                residue
            )

        # CA Coordinates
        elif choice == "8":
            coordinate_calculator(structure,results)

        # Distance Between Residues
        elif choice == "9":
            distance_calculator(structure,results
            )

        # Ligand Analysis
        elif choice == "10":
            ligand_analysis(structure,results)

        # Exit
        elif choice == "11":
            print("\nLeaving Structure Analysis...")
            break

        else:
            print("\nInvalid choice.")