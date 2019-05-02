from . import bparser

def doi_wos_format(bibtex_file):
    bibtex_file = open(bibtex_file,"r")
    bib_database = bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

    dois, nofound = [], []
    for article in bib_database.entries:
        try:
            dois.append(article["doi"])
        except:
            nofound.append(article["title"])

    doi_list=""
    not_found=""

    doi_list+="DO=("
    for doi in dois[:-1]:
        doi_list+=doi
        doi_list+=" OR "
    doi_list+=dois[-1]
    doi_list+=")"

    for title in nofound:
        not_found+=title
        not_found+="; "

    print("WoS formatted: \n", doi_list)
    print("\n")
    print("doi not found: \n", not_found)



