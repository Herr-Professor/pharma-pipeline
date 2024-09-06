# data_collection.py
import requests
import logging

def fetch_api_data(query_params):
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    default_params = {
        "format": "json",
        "fields": "NCTId,BriefTitle,Condition,InterventionName,Phase,OverallStatus",
        "pageSize": 100
    }
    params = {**default_params, **query_params}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('studies', []), data.get('nextPageToken')
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from ClinicalTrials.gov API: {e}")
        return None, None