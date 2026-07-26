from Bio import Entrez
Entrez.email = "017930msbis26@iiu.edu.pk"

# User input
search_term = input("Enter a disease, gene, or keyword: ")
max_results = int(input("Enter the number of articles to retrieve: "))

# Search PubMed
handle = Entrez.esearch(
    db="pubmed",
    term=search_term,
    retmax=max_results
)

record = Entrez.read(handle)
handle.close()

print("\nSearching PubMed...")
print("Total matching articles:", record["Count"])
print("Retrieved articles:", len(record["IdList"]))


if not record["IdList"]:
    print("\nNo articles found for the given search term.")
    exit()


pmids = record["IdList"]
handle = Entrez.efetch(
    db="pubmed",
    id=pmids,
    retmode="xml"
)
records = Entrez.read(handle)
handle.close()

# Output filename
filename = search_term.replace(" ", "_") + "_articles.txt"

# Save titles and abstracts
with open(filename, "w", encoding="utf-8") as file:

    file.write(f"Search Term: {search_term}\n")
    file.write(f"Total Retrieved Articles: {len(pmids)}\n")
    file.write("=" * 70)
    file.write("\n\n")

    for i, article in enumerate(records["PubmedArticle"], start=1):
        citation = article["MedlineCitation"]["Article"]
        pmid = article["MedlineCitation"]["PMID"]
        title = citation["ArticleTitle"]
        journal = citation["Journal"]["Title"]
        year = citation["Journal"]["JournalIssue"]["PubDate"].get(
            "Year", "Unknown"
        )
        file.write(f"Article {i}\n")
        file.write(f"PMID: {pmid}\n")
        file.write(f"Title: {title}\n")
        file.write(f"Journal: {journal}\n")
        file.write(f"Year: {year}\n\n")
        file.write("Abstract:\n")

        if "Abstract" in citation:
            for paragraph in citation["Abstract"]["AbstractText"]:
                file.write(str(paragraph) + "\n")

        else:
            file.write("No abstract available.\n")

        file.write("\n")
        file.write("*" * 70)
        file.write("\n\n")


print(f"\nArticles saved successfully to '{filename}'.")