# config.py
import os

API_URL = "https://clinicaltrials.gov/api/v2/studies"
WEB_URL = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'clinical_trials.db')