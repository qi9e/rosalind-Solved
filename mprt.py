from urllib.request import urlopen
from urllib.error import HTTPError

seq = {}

with open("rosalind_mprt.txt", "r") as f:
    for line in f:
        query = line.strip()
        if not query:
            continue
        accession = query.split("_")[0]

        url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"

        try:
            with urlopen(url) as response:
                doc = response.read().decode("utf-8").splitlines()

            seq[query] = ""
            for row in doc:
                if not row.startswith(">"):
                    seq[query] += row.strip()

        except HTTPError as e:
            print(f"{query} 请求失败: {e}")
            continue

for protein_id in seq:
    motif_point = []

    for i in range(len(seq[protein_id]) - 3):
        fragment = seq[protein_id][i:i+4]

        if (
            fragment[0] == "N"
            and fragment[1] != "P"
            and fragment[2] in ["S", "T"]
            and fragment[3] != "P"
        ):
            motif_point.append(i + 1)

    if motif_point:
        print(protein_id)
        print(" ".join(map(str, motif_point)))