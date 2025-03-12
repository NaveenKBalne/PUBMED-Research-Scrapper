from src.fetch_papers import extract_article_details, save_to_csv

if __name__ == "__main__":
    query = input("Enter your PubMed search query: ")
    papers = extract_article_details(query)
    if papers:
        save_to_csv(papers)
    else:
        print("No results found.")