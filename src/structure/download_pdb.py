import os
import requests

def download_pdb(pdb_id):
    print("\nDownloading PDB structure...")
    url = f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"
    os.makedirs("pdb_files", exist_ok=True)
    filename = os.path.join(
        "pdb_files",
        f"{pdb_id.upper()}.pdb"
    )

    response = requests.get(url)
    if response.status_code != 200:
        print("Download failed.")
        return None

    with open(filename, "w") as file:
        file.write(response.text)
    print("PDB downloaded successfully.")
    print("Saved to:", filename)
    return filename