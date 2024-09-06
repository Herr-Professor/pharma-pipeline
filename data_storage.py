# data_storage.py
import sqlite3
import logging
from datetime import datetime

def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clinical_trials (
        nct_id TEXT PRIMARY KEY,
        brief_title TEXT,
        condition TEXT,
        intervention_name TEXT,
        phase TEXT,
        overall_status TEXT,
        date_processed TEXT
    )
    ''')
    conn.commit()

def store_in_database(data, db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            create_table_if_not_exists(conn)
            cursor = conn.cursor()
            for _, row in data.iterrows():
                cursor.execute('''
                INSERT OR REPLACE INTO clinical_trials 
                (nct_id, brief_title, condition, intervention_name, phase, overall_status, date_processed)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['NCTId'],
                    row['BriefTitle'],
                    ', '.join(row['Condition']) if isinstance(row['Condition'], list) else (row['Condition'] or ''),
                    ', '.join(row['InterventionName']) if isinstance(row['InterventionName'], list) else (row['InterventionName'] or ''),
                    row['Phase'] or '',
                    row['OverallStatus'] or '',
                    datetime.now().isoformat()
                ))
            conn.commit()
        logging.info(f"Successfully stored {len(data)} records in the database.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while storing data in the database: {e}")
        raise