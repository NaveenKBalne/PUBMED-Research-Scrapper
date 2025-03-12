# import requests
# import pandas as pd
# from src.utils import fetch_pubmed_articles

# def extract_article_details(query):
#     articles = fetch_pubmed_articles(query)
#     if not articles:
#         return []

#     results = []
#     for article in articles["PubmedArticleSet"]["PubmedArticle"]:
#         pubmed_id = article["MedlineCitation"]["PMID"]["#text"]
#         title = article["MedlineCitation"]["Article"]["ArticleTitle"]
#         pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
        
#         # Placeholder for non-academic author filtering (to be implemented)
#         non_academic_authors = "N/A"
#         company_affiliations = "N/A"
#         corresponding_email = "N/A"

#         results.append([pubmed_id, title, pub_date, non_academic_authors, company_affiliations, corresponding_email])
    
#     return results

# def save_to_csv(data, filename="data/research_papers.csv"):
#     df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")



# import requests
# import pandas as pd
# from src.utils import fetch_pubmed_articles

# def extract_article_details(query):
#     articles = fetch_pubmed_articles(query)
#     if not articles:
#         return []

#     results = []
#     for pmid, details in articles.items():  # Iterate through the dictionary
#         if pmid == "header" or pmid == "result":  # Skip header and result keys
#             continue

#         try:
#             # Extract relevant details safely
#             pubmed_id = details["uid"]
#             title = details["title"]
#             pub_date = details["pubdate"]

#             # Placeholder for non-academic author filtering (to be implemented)
#             non_academic_authors = "N/A"
#             company_affiliations = "N/A"
#             corresponding_email = "N/A"

#             results.append([pubmed_id, title, pub_date, non_academic_authors, company_affiliations, corresponding_email])
#         except KeyError as e:
#             print(f"KeyError: {e} - Skipping article with PMID: {pmid}")
#             continue #skip the article that has a key error.

#     return results

# def save_to_csv(data, filename="data/research_papers.csv"):
#     df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")



# import requests
# import pandas as pd
# from src.utils import fetch_pubmed_articles

# def extract_article_details(query):
#     articles = fetch_pubmed_articles(query)
#     if not articles:
#         return []

#     results = []
#     if "result" in articles and "uids" in articles["result"]: #check if the result key exists.
#         for pmid in articles["result"]["uids"]: #iterate through the uids.
#             if pmid in articles["result"]: #check if the pmid key exists in the result dictionary.
#                 details = articles["result"][pmid]
#                 try:
#                     pubmed_id = details["uid"]
#                     title = details["title"]
#                     pub_date = details["pubdate"]

#                     non_academic_authors = "N/A"
#                     company_affiliations = "N/A"
#                     corresponding_email = "N/A"

#                     results.append([pubmed_id, title, pub_date, non_academic_authors, company_affiliations, corresponding_email])
#                 except KeyError as e:
#                     print(f"KeyError: {e} - Skipping article with PMID: {pmid}")
#                     continue
#             else:
#                 print(f"PMID {pmid} not found in results.")
#     else:
#         print("No results or uids found in articles.")

#     return results

# def save_to_csv(data, filename="data/research_papers.csv"):
#     df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")


# import requests
# import pandas as pd
# from src.utils import fetch_pubmed_articles

# def extract_article_details(query):
#     articles = fetch_pubmed_articles(query)
#     if not articles:
#         return []

#     results = []
#     if "result" in articles and "uids" in articles["result"]:
#         for pmid in articles["result"]["uids"]:
#             if pmid in articles["result"]:
#                 details = articles["result"][pmid]
#                 try:
#                     pubmed_id = details["uid"]
#                     title = details["title"]
#                     pub_date = details["pubdate"]

#                     # Placeholder for non-academic author filtering (to be implemented)
#                     non_academic_authors = "N/A"
#                     company_affiliations = "N/A"
#                     corresponding_email = "N/A"

#                     # Extract authors and affiliations (basic example - improve as needed)
#                     authors = details.get("authors", [])
#                     non_academic_authors_list = []
#                     company_affiliations_list = []

#                     for author in authors:
#                         # This is a very basic example - improve logic for detecting company/non-academic
#                         if "Pfizer" in str(author.get("name", "")) or "BioNTech" in str(author.get("name", "")): # basic company detection
#                             company_affiliations_list.append(author.get("name", ""))
#                         # Example of how to detect non academic. This example is very basic, and will need to be improved.
#                         # if some_condition_indicating_non_academic:
#                         #     non_academic_authors_list.append(author.get("name", ""))

#                     non_academic_authors = ", ".join(non_academic_authors_list)
#                     company_affiliations = ", ".join(company_affiliations_list)

#                     results.append([pubmed_id, title, pub_date, non_academic_authors, company_affiliations, corresponding_email])
#                 except KeyError as e:
#                     print(f"KeyError: {e} - Skipping article with PMID: {pmid}")
#                     continue
#             else:
#                 print(f"PMID {pmid} not found in results.")
#     else:
#         print("No results or uids found in articles.")

#     return results

# def save_to_csv(data, filename="data/research_papers.csv"):
#     df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")

# # Example usage (in your main.py or similar):
# if __name__ == "__main__":
#     query = '"COVID-19 vaccine" AND Pfizer'
#     papers = extract_article_details(query)
#     if papers:
#         save_to_csv(papers)


# import requests
# import pandas as pd
# import xml.etree.ElementTree as ET
# import re
# from src.utils import fetch_pubmed_articles

# def get_full_article_details(pmid):
#     """Fetches full article details from PubMed using efetch."""
#     url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
#         return response.content
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching article details for PMID {pmid}: {e}")
#         return None

# def extract_article_details(query):
#     articles = fetch_pubmed_articles(query)
#     if not articles or "result" not in articles or "uids" not in articles["result"]:
#         print("No results or invalid response from esummary.")
#         return []

#     results = []
#     for pmid in articles["result"]["uids"]:
#         if pmid not in articles["result"]:
#             print(f"PMID {pmid} not found in esummary results.")
#             continue

#         details = articles["result"][pmid]
#         try:
#             pubmed_id = details["uid"]
#             title = details["title"]
#             pub_date = details["pubdate"]

#             xml_data = get_full_article_details(pmid)
#             if xml_data:
#                 tree = ET.fromstring(xml_data)
#                 non_academic_authors, company_affiliations = extract_affiliations(tree)
#                 corresponding_email = extract_email(tree)

#                 results.append([pubmed_id, title, pub_date, ", ".join(non_academic_authors), ", ".join(company_affiliations), corresponding_email])
#             else:
#                 results.append([pubmed_id, title, pub_date, "N/A", "N/A", "N/A"]) #add NA if efetch fails.

#         except KeyError as e:
#             print(f"KeyError: {e} - Skipping article with PMID: {pmid}")
#             continue

#     return results

# def extract_affiliations(tree):
#     non_academic_authors = []
#     company_affiliations = []
#     seen_affiliations = set()

#     for author in tree.findall(".//Author"):
#         affiliations = author.findall(".//AffiliationInfo/Affiliation")
#         for affiliation in affiliations:
#             affiliation_text = affiliation.text.strip().lower()

#             if affiliation_text in seen_affiliations:
#                 continue
#             seen_affiliations.add(affiliation_text)

#             if re.search(r"(pfizer|biontech|merck|novartis|biogen)", affiliation_text):
#                 company_affiliations.append(affiliation.text.strip())
#             elif not re.search(r"(university|college|institute|hospital|center)", affiliation_text):

#                 #Remove address like data.
#                 cleaned_affiliation = re.sub(r",\s*\d+\s+[A-Z][a-z]+(\s+[A-Z][a-z]+)*\s*$", "", affiliation.text.strip())

#                 #Remove extra punctuation.
#                 cleaned_affiliation = re.sub(r"[,.]+$", "", cleaned_affiliation)

#                 #Remove extra whitespace.
#                 cleaned_affiliation = " ".join(cleaned_affiliation.split())

#                 #Remove redundant phrases.
#                 cleaned_affiliation = re.sub(r"(department of|division of|laboratory of|unit of|section of)\s*", "", cleaned_affiliation, flags=re.IGNORECASE)

#                 #Remove redundant locations.
#                 cleaned_affiliation = re.sub(r"amsterdam, the netherlands", "", cleaned_affiliation, flags=re.IGNORECASE)

#                 #Remove leftover periods.
#                 cleaned_affiliation = re.sub(r"\.\s*\.", ".", cleaned_affiliation)

#                 #Remove any trailing or leading periods
#                 cleaned_affiliation = cleaned_affiliation.strip('.')

#                 #Remove empty values.
#                 cleaned_affiliation = re.sub(r"^\s*$", "", cleaned_affiliation)

#                 #Remove empty values between commas.
#                 cleaned_affiliation = re.sub(r",\s*,+", ",", cleaned_affiliation)

#                 #Truncate long strings.
#                 if len(cleaned_affiliation) > 200:
#                     cleaned_affiliation = cleaned_affiliation[:200] + "..."

#                 if cleaned_affiliation:
#                     non_academic_authors.append(cleaned_affiliation)

#             for author in tree.findall(".//Author"):
#              affiliations = author.findall(".//AffiliationInfo/Affiliation")
#             for affiliation in affiliations:
#                 affiliation_text = affiliation.text.strip().lower()

#             if affiliation_text in seen_affiliations:
#                 continue
#             seen_affiliations.add(affiliation_text)

#             if re.search(r"(pfizer|biontech|merck|novartis|biogen)", affiliation_text):
#                 company_affiliations.append(affiliation.text.strip())
#             elif not re.search(r"(university|college|institute|hospital|center)", affiliation_text):

#                 # ... (regex cleaning steps) ...

#                 # Debugging print statements
#                 print(f"Affiliation Text: {affiliation_text}")
#                 print(f"Cleaned Affiliation: {cleaned_affiliation}")

#                 if cleaned_affiliation:
#                     non_academic_authors.append(cleaned_affiliation)

#     return non_academic_authors, company_affiliations

#     return non_academic_authors, company_affiliations

# def extract_email(tree):
#     article_text = ET.tostring(tree, encoding='unicode').lower()

#     # Improved corresponding author detection
#     corresponding_author_match = re.search(r"(corresponding author|contact author|to whom correspondence should be addressed).*?([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", article_text)
#     if corresponding_author_match:
#         return corresponding_author_match.group(2)

#     # Prioritize emails in affiliations
#     affiliation_emails = re.findall(r"affiliation.*?([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", article_text)
#     if affiliation_emails:
#         return affiliation_emails[0]

#     # Basic email extraction (fallback)
#     emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", article_text)
#     if emails:
#         return emails[0]
#     else:
#         return "N/A"

# def save_to_csv(data, filename="data/research_papers.csv"):
#     df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")

# if __name__ == "__main__":
#     query = '"Alzheimer\'s disease" AND (Biogen OR Novartis OR Merck OR Pfizer)'
#     papers = extract_article_details(query)
#     if papers:
#         save_to_csv(papers)






import requests
import pandas as pd
import xml.etree.ElementTree as ET
import re
from src.utils import fetch_pubmed_articles  # Assuming fetch_pubmed_articles is in src/utils.py

def get_full_article_details(pmid):
    """Fetches full article details from PubMed using efetch."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article details for PMID {pmid}: {e}")
        return None

def extract_article_details(query):
    articles = fetch_pubmed_articles(query)
    if not articles or "result" not in articles or "uids" not in articles["result"]:
        print("No results or invalid response from esummary.")
        return []

    results = []
    for pmid in articles["result"]["uids"]:
        if pmid not in articles["result"]:
            print(f"PMID {pmid} not found in esummary results.")
            continue

        details = articles["result"][pmid]
        try:
            pubmed_id = details["uid"]
            title = details["title"]
            pub_date = details["pubdate"]

            xml_data = get_full_article_details(pmid)
            if xml_data:
                tree = ET.fromstring(xml_data)
                non_academic_authors, company_affiliations = extract_affiliations(tree)
                corresponding_email = extract_email(tree)

                results.append([pubmed_id, title, pub_date, ", ".join(non_academic_authors), ", ".join(company_affiliations), corresponding_email])
            else:
                results.append([pubmed_id, title, pub_date, "N/A", "N/A", "N/A"]) #add NA if efetch fails.

        except KeyError as e:
            print(f"KeyError: {e} - Skipping article with PMID: {pmid}")
            continue

    return results

def extract_affiliations(tree):
    """Extracts non-academic and company affiliations from the XML tree."""
    non_academic_authors = []
    company_affiliations = []
    seen_affiliations = set()

    for author in tree.findall(".//Author"):
        affiliations = author.findall(".//AffiliationInfo/Affiliation")
        for affiliation in affiliations:
            affiliation_text = affiliation.text.strip().lower()

            if affiliation_text in seen_affiliations:
                continue
            seen_affiliations.add(affiliation_text)

            if re.search(r"(pfizer|biontech|merck|novartis|biogen)", affiliation_text):
                company_affiliations.append(affiliation.text.strip())
            elif not re.search(r"(university|college|institute|hospital|center)", affiliation_text):

                cleaned_affiliation = affiliation_text

                #Remove address like data.
                cleaned_affiliation = re.sub(r",\s*\d+\s+[A-Z][a-z]+(\s+[A-Z][a-z]+)*\s*$", "", cleaned_affiliation)

                #Remove extra punctuation.
                cleaned_affiliation = re.sub(r"[,.]+$", "", cleaned_affiliation)

                #Remove extra whitespace.
                cleaned_affiliation = " ".join(cleaned_affiliation.split())

                #Remove redundant phrases.
                cleaned_affiliation = re.sub(r"(department of|division of|laboratory of|unit of|section of)\s*", "", cleaned_affiliation, flags=re.IGNORECASE)

                #Remove redundant locations.
                cleaned_affiliation = re.sub(r"amsterdam, the netherlands", "", cleaned_affiliation, flags=re.IGNORECASE)

                #Remove leftover periods.
                cleaned_affiliation = re.sub(r"\.\s*\.", ".", cleaned_affiliation)

                #Remove any trailing or leading periods
                cleaned_affiliation = cleaned_affiliation.strip('.')

                #Remove empty values.
                cleaned_affiliation = re.sub(r"^\s*$", "", cleaned_affiliation)

                #Remove empty values between commas.
                cleaned_affiliation = re.sub(r",\s*,+", ",", cleaned_affiliation)

                #Truncate long strings.
                if len(cleaned_affiliation) > 200:
                    cleaned_affiliation = cleaned_affiliation[:200] + "..."

                if cleaned_affiliation:
                    non_academic_authors.append(cleaned_affiliation)
            else:
                cleaned_affiliation = "Academic Institution"

            # Debugging print statements
            print(f"Affiliation Text: {affiliation_text}")
            print(f"Cleaned Affiliation: {cleaned_affiliation}")

    return non_academic_authors, company_affiliations

def extract_email(tree):
    article_text = ET.tostring(tree, encoding='unicode').lower()

    # Improved corresponding author detection
    corresponding_author_match = re.search(r"(corresponding author|contact author|to whom correspondence should be addressed).*?([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", article_text)
    if corresponding_author_match:
        return corresponding_author_match.group(2)

    # Prioritize emails in affiliations
    affiliation_emails = re.findall(r"affiliation.*?([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", article_text)
    if affiliation_emails:
        return affiliation_emails[0]

    # Basic email extraction (fallback)
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", article_text)
    if emails:
        return emails[0]
    else:
        return "N/A"

def save_to_csv(data, filename="data/research_papers.csv"):
    df = pd.DataFrame(data, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    query = '"Alzheimer\'s disease" AND (Biogen OR Novartis OR Merck OR Pfizer)'
    papers = extract_article_details(query)
    if papers:
        save_to_csv(papers)