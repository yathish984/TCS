import requests

API_KEY = "ghfkffu6378382826hhdjgk"
BASE_URL = "https://bluemutualfund.in/server/api/company.php"

def fetch_company_data(company_id):
    params = {
        "id": company_id,
        "api_key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data for", company_id)
        return None
