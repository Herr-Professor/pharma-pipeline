# main.py
import logging
from config import DB_PATH
from data_collection import fetch_api_data
from data_processing import process_data, validate_data, transform_data_for_db
from data_storage import store_in_database
from data_analysis import analyze_data
from reporting import generate_report

logging.basicConfig(filename='pipeline.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting data pipeline")

        # User input
        search_query = input("Enter your search query for clinical trials: ")
        
        # Data Collection
        logging.info(f"Fetching API data for query: {search_query}")
        all_studies = []
        next_page_token = None
        while True:
            studies, next_page_token = fetch_api_data({"query.term": search_query, "pageToken": next_page_token})
            if studies:
                all_studies.extend(studies)
            if not next_page_token:
                break
        
        logging.info(f"Fetched {len(all_studies)} studies from API")

        # Data Processing
        logging.info("Processing collected data")
        processed_data = process_data(all_studies)

        # Add this after processing the data
        logging.info(f"Columns in processed data: {processed_data.columns.tolist()}")
        logging.info(f"First few rows of processed data:\n{processed_data.head().to_string()}")

        # Data Validation
        logging.info("Validating processed data")
        if not validate_data(processed_data):
            raise ValueError("Data validation failed. Check the log for details.")

        # Data Transformation
        logging.info("Transforming data for database insertion")
        transformed_data = transform_data_for_db(processed_data)

        # Data Storage
        logging.info("Storing data in database")
        store_in_database(transformed_data, DB_PATH)

        # Data Analysis
        logging.info("Performing data analysis")
        analysis_results = analyze_data(processed_data)
        
        # Reporting
        logging.info("Generating report")
        generate_report(analysis_results, search_query)

        logging.info("Data pipeline completed successfully")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()