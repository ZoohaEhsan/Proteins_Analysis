# Proteins_Analysis

A Python and Biopython project for exploring protein sequence and structure data.

This project brings together several small bioinformatics modules into an interactive workflow. It can retrieve gene records from NCBI, extract protein sequences, find UniProt and PDB information, download PDB structures, and perform basic protein structure analysis.

## Workflow

The project follows this general workflow:

```text
Gene Symbol
    ↓
NCBI / GenBank
    ↓
Protein Sequence
    ↓
UniProt
    ↓
PDB Cross-References
    ↓
PDB Structure
    ↓
Structure Analysis
    ↓
CSV Results
```

## Tech Stack

- **Language:** Python 3
- **Libraries:** Biopython, Requests
- **Data sources:** NCBI, UniProt, RCSB PDB
- **Interface:** Command-line interface (CLI)

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Install Dependencies

```bash
pip install biopython requests
```

### Before First Run

Set your email address in:

```text
src/sequence/retrieve_gene_data.py
```

Replace:

```python
Entrez.email = "enter email"
```

with your email address.

The program also requires a `data/` directory in the repository root because GenBank and FASTA files are saved there.

Create it with:

```bash
mkdir data
```

### Run the Project

From the repository root:

```bash
python main.py
```

The program runs interactively and guides the user through the workflow.

Typical prompts include:

- Enter gene symbol (e.g., `TP53`)
- Enter organism (e.g., `Homo sapiens`)
- Enter the number of records to retrieve
- Select a record
- Select a PDB structure
- Select structural analyses

## Outputs

Depending on the selected analysis, the program generates:

- **GenBank file:** `data/{GENE}.gb`
- **Protein FASTA:** `data/{GENE}_protein.fasta`
- **PDB structure:** `pdb_files/{PDBID}.pdb`
- **Analysis report:** `{GENE}_analysis_results.csv`

## Project Structure

```text
Proteins_Analysis/
│
├── main.py
│
├── src/
│   ├── sequence/
│   │   ├── retrieve_gene_data.py
│   │   └── search_uniprot.py
│   │
│   └── structure/
│       ├── download_pdb.py
│       ├── structure_reader.py
│       ├── structure_menu.py
│       ├── coordinates_calculator.py
│       ├── distance_calculator.py
│       └── ligand_search.py
│
├── data/
├── pdb_files/
├── README.md
```

## Modules

### Sequence Analysis

- `retrieve_gene_data.py` — Searches NCBI using Entrez, retrieves GenBank records, and extracts protein sequences.
- `search_uniprot.py` — Searches UniProt for protein information and retrieves PDB cross-references.

### Structure Analysis

- `download_pdb.py` — Downloads selected protein structures from the RCSB PDB.
- `structure_reader.py` — Parses PDB structures using Biopython and provides information about chains, residues, and atoms.
- `structure_menu.py` — Provides an interactive menu for selecting structural analyses.
- `coordinates_calculator.py` — Works with atomic coordinates.
- `distance_calculator.py` — Calculates distances between atoms or residues.
- `ligand_search.py` — Identifies and lists ligands present in a structure.

## Usage Example

1. Run the program:

```bash
python main.py
```

2. Enter a gene symbol, for example:

```text
TP53
```

3. Enter the organism:

```text
Homo sapiens
```

4. Select a GenBank record.

5. Select a PDB structure from the available cross-references.

6. The selected PDB structure is downloaded and parsed.

7. Use the structure menu to perform analyses such as:

   - Chain information
   - Residue information
   - Atom information
   - Coordinate calculations
   - Distance calculations
   - Ligand identification

8. Analysis results are exported to a CSV file.

## Why I Built This

This project is part of my learning journey in bioinformatics and Python.

I built it to practice working with biological databases, APIs, Biopython, protein sequences, and 3D protein structures while gradually turning individual scripts into a connected workflow.

It is a learning project and will continue to evolve as I explore more bioinformatics concepts and Python programming.

## Notes

- NCBI Entrez requires a valid email address.
- Internet access is required because the project retrieves information from NCBI, UniProt, and RCSB PDB.
- API requests may occasionally fail or be rate-limited. If this happens, retry after some time.
- Some PDB structures may contain non-standard atoms, chains, or multiple models that require additional handling.
