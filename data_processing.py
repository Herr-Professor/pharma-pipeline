# data_processing.py
import pandas as pd
import logging

def process_data(api_data):
    df = pd.DataFrame(api_data)
    
    def safe_get_interventions(x):
        try:
            return [i['name'] for i in x['armsInterventionsModule'].get('interventions', [])]
        except KeyError:
            return []

    # Extract required fields from the nested structure
    processed_data = pd.DataFrame({
        'NCTId': df['protocolSection'].apply(lambda x: x['identificationModule']['nctId']),
        'BriefTitle': df['protocolSection'].apply(lambda x: x['identificationModule']['briefTitle']),
        'Phase': df['protocolSection'].apply(lambda x: x['designModule'].get('phases', ['N/A'])[0]),
        'OverallStatus': df['protocolSection'].apply(lambda x: x['statusModule']['overallStatus']),
        'Condition': df['protocolSection'].apply(lambda x: x['conditionsModule'].get('conditions', [])),
        'InterventionName': df['protocolSection'].apply(safe_get_interventions)
    })
    
    return processed_data

def validate_data(data):
    required_columns = ['NCTId', 'BriefTitle', 'Phase', 'OverallStatus']
    
    if data.empty:
        logging.error("Validation failed: Dataset is empty")
        return False
    
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.error(f"Validation failed: Missing required columns: {', '.join(missing_columns)}")
        return False
    
    # Additional checks can be added here, e.g., data type validation
    
    return True

def transform_data_for_db(data):
    data['date_processed'] = pd.Timestamp.now()
    return data