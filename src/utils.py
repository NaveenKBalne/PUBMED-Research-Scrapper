# import requests
# from config import API_KEY, PUBMED_BASE_URL  # ✅ Import API Key & Base URL

# def fetch_pubmed_articles(query):
#     params = {
#         "db": "pubmed",
#         "term": query,  # User search query
#         "retmode": "json",
#         "retmax": 10,  # Number of results to fetch
#         "api_key": API_KEY  # ✅ Pass API Key in request
#     }

#     # ✅ Construct request URL
#     # full_url = f"{PUBMED_BASE_URL}?db=pubmed&term={query}&retmode=json&retmax=10&api_key={API_KEY}"
#     full_url = f"{PUBMED_BASE_URL}?db=pubmed&term={encoded_query}&retmode=json&retmax=10&api_key={API_KEY}"
    

#     print("Request URL:", full_url)  # ✅ Debugging print statement
    
#     response = requests.get(full_url)

#     if response.status_code != 200:
#         print(f"Error fetching data: {response.status_code}")
#         return None

#     return response.json()

# 2ND
# import requests
# import urllib.parse  # ✅ Import for encoding the query
# from config import API_KEY, PUBMED_BASE_URL  

# def fetch_pubmed_articles(query):
#     encoded_query = urllib.parse.quote(query)  # ✅ URL-encode query
#     params = {
#         "db": "pubmed",
#         "term": encoded_query,  
#         "retmode": "json",
#         "retmax": 10,  
#         "api_key": API_KEY  
#     }

#     # ✅ Construct request URL properly
#     full_url = f"{PUBMED_BASE_URL}?db=pubmed&term={encoded_query}&retmode=json&retmax=10&api_key={API_KEY}"
    
#     print("Request URL:", full_url)  # ✅ Debugging print statement
    
#     response = requests.get(full_url)

#     if response.status_code != 200:
#         print(f"Error fetching data: {response.status_code}")
#         return None

#     return response.json()


# 







# import urllib.parse
# import requests
# from config import API_KEY, PUBMED_BASE_URL, FETCH_DETAILS_URL

# def fetch_pubmed_articles(query):
#     """
#     Fetches PubMed articles based on a search query.

#     Args:
#         query (str): The search query.

#     Returns:
#         dict: JSON response containing article details, or None if an error occurs.
#     """
#     encoded_query = urllib.parse.quote(query)
#     params = {
#         "db": "pubmed",
#         "term": encoded_query,
#         "retmode": "json",
#         "retmax": 10,
#         "api_key": API_KEY,
#     }

#     search_url = f"{PUBMED_BASE_URL}?db=pubmed&term={encoded_query}&retmode=json&retmax=10&api_key={API_KEY}"
#     print("Request URL:", search_url)

#     try:
#         response = requests.get(search_url)
#         print("Response Status Code:", response.status_code)

#         try:
#             data = response.json()
#             print("Response JSON:", data)
#         except requests.exceptions.JSONDecodeError:
#             print("Response Text:", response.text)

#         response.raise_for_status()  # Raise HTTPError for bad responses

#         data = response.json()
#         pmids = data.get("esearchresult", {}).get("idlist", [])

#         if not pmids:
#             print("No results found.")
#             return None

#         pmid_str = ",".join(pmids)
#         details_url = f"{FETCH_DETAILS_URL}?db=pubmed&id={pmid_str}&retmode=json&api_key={API_KEY}"
#         print("Fetching details from:", details_url)

#         response_details = requests.get(details_url)
#         response_details.raise_for_status() # Raise HTTPError for bad responses.

#         return response_details.json()

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return None



import urllib.parse
import requests
from config import API_KEY, PUBMED_BASE_URL, FETCH_DETAILS_URL

def fetch_pubmed_articles(query):
    """
    Fetches PubMed articles based on a search query.

    Args:
        query (str): The search query.

    Returns:
        dict: JSON response containing article details, or None if an error occurs.
    """
    encoded_query = urllib.parse.quote(query)
    params = {
        "db": "pubmed",
        "term": encoded_query,
        "retmode": "json",
        "retmax": 10,
        "api_key": API_KEY,
    }

    search_url = f"{PUBMED_BASE_URL}?db=pubmed&term={encoded_query}&retmode=json&retmax=10&api_key={API_KEY}"
    print("Request URL:", search_url)

    try:
        response = requests.get(search_url)
        print("Response Status Code:", response.status_code)

        try:
            data = response.json()
            print("Response JSON:", data)
        except requests.exceptions.JSONDecodeError:
            print("Response Text:", response.text)

        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        pmids = data.get("esearchresult", {}).get("idlist", [])

        if not pmids:
            print("No results found.")
            return None

        pmid_str = ",".join(pmids)
        details_url = f"{FETCH_DETAILS_URL}?db=pubmed&id={pmid_str}&retmode=json&api_key={API_KEY}"
        print("Fetching details from:", details_url)

        response_details = requests.get(details_url)
        print("ESummary Response Status Code:", response_details.status_code)
        try:
            details_data = response_details.json()
            print("ESummary Response JSON:", details_data)
        except requests.exceptions.JSONDecodeError:
            print("ESummary Response Text:", response_details.text)

        response_details.raise_for_status()
        # response_details.raise_for_status()

        details_data = response_details.json()
        return details_data #return the details data.

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    



