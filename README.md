# PubMed Research Paper Extractor

This Python script extracts research paper details from PubMed based on a user-defined query and saves the results to a CSV file. It fetches article titles, publication dates, non-academic author affiliations, company affiliations, and corresponding author emails.

## Features

-   Fetches PubMed articles using the NCBI E-utilities API.
-   Extracts key article details: PubMed ID, title, publication date.
-   Identifies and extracts non-academic and company affiliations.
-   Extracts corresponding author emails using regular expressions.
-   Saves extracted data to a CSV file.
-   Robust error handling for API requests and XML parsing.
-   Cleans and formats affiliation data.

## Prerequisites

-   Python 3.x
-   `requests` library (`pip install requests`)
-   `pandas` library (`pip install pandas`)

## Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Ensure you have the required libraries installed:**

    ```bash
    pip install requests pandas
    ```

3.  **Create a `src` folder with a `utils.py` file:**
    * This file should contain the function `fetch_pubmed_articles` that calls the esummary api.
    * Example of `src/utils.py`:

    ```python
    import requests
    import json

    def fetch_pubmed_articles(query):
        """Fetches PubMed articles based on a query."""
        base_url = "[https://eutils.ncbi.nlm.nih.gov/entrez/eutils/](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)"
        search_url = f"{base_url}esearch.fcgi?db=pubmed&term={query}&retmode=json"

        try:
            response = requests.get(search_url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            search_data = response.json()

            if "esearchresult" in search_data and "idlist" in search_data["esearchresult"]:
                id_list = search_data["esearchresult"]["idlist"]
                if not id_list:
                    return None  # No results found

                summary_url = f"{base_url}esummary.fcgi?db=pubmed&id={','.join(id_list)}&retmode=json"
                summary_response = requests.get(summary_url)
                summary_response.raise_for_status()
                summary_data = summary_response.json()
                return summary_data
            else:
                return None  # Invalid search data format

        except requests.exceptions.RequestException as e:
            print(f"Error fetching PubMed articles: {e}")
            return None
    ```

4.  **Run the script:**

    ```bash
    python main.py
    ```

5.  **Modify the query:**
    * Open `main.py` and change the `query` variable in the `if __name__ == "__main__":` block to your desired search query.
    * Modify the `filename` variable in the `save_to_csv` function to change the output CSV filename.

6.  **Find your results:**
    * The results will be saved in a CSV file named `data/research_papers.csv` (or your specified filename).

## Code Structure

-   `main.py`: Main script to execute the PubMed data extraction.
-   `src/utils.py`: Utility functions, including `fetch_pubmed_articles`.
-   `data/research_papers.csv`: Output CSV file containing the extracted data.

## Functionality

-   `get_full_article_details(pmid)`: Fetches full article XML from PubMed.
-   `extract_article_details(query)`: Orchestrates the extraction process.
-   `extract_affiliations(tree)`: Extracts and cleans non-academic and company affiliations.
-   `extract_email(tree)`: Extracts corresponding author emails.
-   `save_to_csv(data, filename)`: Saves the extracted data to a CSV file.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.
