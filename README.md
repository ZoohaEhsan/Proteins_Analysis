# Proteins_Analysis

A lightweight interactive toolkit to fetch protein sequences (from NCBI), find UniProt and PDB cross-references, download PDB files, and perform basic structural inspections using Biopython.

## What this is
Proteins_Analysis is a CLI-driven collection of small modules that walk a user through: retrieving nucleotide/genbank records, extracting protein sequences, locating UniProt and PDB entries, downloading a PDB file, and running basic structural analyses (chain/residue/atom summaries and simple coordinate/distance utilities).

### Stack
- Language(s): Python 3
- Notable libraries: Biopython, requests
- Runtime: CLI / single-script orchestration (`main.py`)

## Quick start

Prerequisites
- Python 3.8+
- pip

Install dependencies:
```bash
pip install biopython requests
```

Before first run:
- Set Entrez email in `src/sequence/retrieve_gene_data.py` (replace `"enter email"` with your email).
- Create a `data/` directory in the repo root (the code writes GenBank and FASTA files there).
```bash
mkdir -p data
```

Run:
```bash
python main.py
```

The script runs interactively. Typical session prompts:
- Enter gene symbol: (e.g., TP53)
- Enter organism (e.g., Homo sapiens)
- Enter the number of records to retrieve (Press Enter for 5)
- Select a record number
- Select a PDB structure

Outputs:
- GenBank file: data/{GENE}.gb
- Protein FASTA: data/{GENE}_protein.fasta
- Downloaded PDB file: pdb_files/{PDBID}.pdb
- Analysis CSV: {GENE}_analysis_results.csv (contains summary analyses produced via the structure menu)

## Project layout
Top-level:
- main.py            — orchestrates the 5-step workflow (sequence → UniProt → PDB → structure reading → analyses export)
- src/
  - sequence/        — sequence retrieval & UniProt lookup
    - retrieve_gene_data.py  — NCBI Entrez search, saves GenBank and protein FASTA
    - search_uniprot.py      — query UniProt REST API, list PDB cross-references
  - structure/       — PDB download, reading, and analyses
    - download_pdb.py         — downloads PDB from RCSB (creates `pdb_files/`)
    - structure_reader.py     — parse PDB and provides functions for chains/residues/atoms
    - structure_menu.py       — interactive selection of structural analyses (integrates calculators)
    - distance_calculator.py  — distance calculations between atoms/residues
    - coordinates_calculator.py — coordinate utilities
    - ligand_search.py        — ligand detection / listing utilities
- .idea/              — IDE settings (can be ignored or removed)

## What each module does (high level)
- main.py:
  - Calls `retrieve_gene_data()` to fetch nucleotide / genbank and extract protein info.
  - Calls `search_uniprot()` to get UniProt accession and candidate PDB IDs.
  - Downloads selected PDB via `download_pdb()`.
  - Uses `read_structure()` to parse PDB (Biopython PDBParser) and then invokes `structure_menu()` to let the user choose analyses.
  - Exports results list to `{gene}_analysis_results.csv`.

- src/sequence/retrieve_gene_data.py:
  - Uses Biopython Entrez to search NCBI nucleotide, fetches GenBank, extracts the CDS for the requested gene, saves GenBank and protein FASTA to `data/`.

- src/sequence/search_uniprot.py:
  - Queries UniProt REST API for the protein accession, extracts UniProt id, name, organism, lists PDB cross-references (fetches metadata from RCSB for titles/organism).

- src/structure/download_pdb.py:
  - Downloads PDB file from `files.rcsb.org` and saves to `pdb_files/`.

- src/structure/structure_reader.py:
  - Reads TITLE lines and builds a Biopython Structure object.
  - Provides functions used by `structure_menu`:
    - list_chains, count_chains
    - list_residues, count_residues, first_ten_residues, last_amino_acid
    - list_atoms_in_residue
  - Additional modules implement coordinate/distance/ligand utilities.

## Usage example (minimal)
1. Ensure dependencies installed and `data/` exists.
2. Run `python main.py`.
3. Follow prompts:
   - Enter gene symbol: BRCA1
   - Enter organism: Homo sapiens
   - (choose results and PDB)
4. After picking a PDB, the PDB is downloaded to `pdb_files/`, the structure parsed, and the structure menu appears to run analyses. Results saved to CSV.

## Notes & tips
- Entrez requires a valid email. Set `Entrez.email` in `src/sequence/retrieve_gene_data.py`.
- The code creates `pdb_files/` automatically, but it does not create `data/`; create it beforehand to avoid file write errors.
- Network/API errors: NCBI, UniProt or RCSB requests may fail or be rate-limited. If a request fails, check status and retry later.
- PDB parsing: non-standard atom/chain labels or multi-model entries may require additional handling; Biopython PDBParser errors may surface for odd files.

## Suggested improvements (low-effort)
- Add a `requirements.txt` or pyproject for reproducible installs.
- Create a non-interactive mode (CLI flags) for scripted runs.
- Ensure `data/` is created programmatically in `retrieve_gene_data.py`.
- Move Entrez.email to config/env var (e.g., ENTIREZ_EMAIL) to avoid hardcoding.
- Add unit tests for any deterministic parsing utilities (distance/coordinate computations).

## Contributing
- Fork, add tests for new features, open a pull request.
- Please include sample input and expected output for parsing/analysis features.

## License
Add a license file (e.g., MIT) if you intend this to be open-source. Currently none is present.

## Contact
Repository owner: @ZoohaEhsan
