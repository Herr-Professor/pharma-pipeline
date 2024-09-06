# README.md
# Pharmaceutical Research Data Pipeline

This project is a Python-based data pipeline designed to collect, process, store, and analyze data relevant to pharmaceutical research, with a focus on clinical trials.

## Features
- Fetches data from the ClinicalTrials.gov API
- Scrapes the latest situation report link from the WHO website
- Processes and combines data from multiple sources
- Stores processed data in a sqllite database
- Performs basic data analysis and generates visualizations
- Creates a summary report of the analysis

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pharma-research-pipeline.git
   cd pharma-research-pipeline
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```
python main.py
```

This will execute the entire pipeline:
1. Fetch data from the ClinicalTrials.gov API
2. Process and combine the data
3. Validate the data
4. Store the results in the sqllite database
5. Perform data analysis
6. Generate a report and visualization

## Output

- `pipeline.log`: Log file with information about the pipeline execution
- `pipeline_report.txt`: Text report with summary statistics
- `trials_by_phase.png`: Pie chart visualizing the distribution of trials by phase

## Customization

- To modify the API data fetching, edit the `fetch_api_data` function in `data_collection.py`.
- To change the web scraping logic, modify the `scrape_web_data` function in `data_collection.py`.
- To adjust data processing, update the `process_data` function in `data_processing.py`.
- To change how data is stored, edit the `store_in_database` function in `data_storage.py`.
- To modify the analysis, update the `analyze_data` function in `data_analysis.py`.
- To change the report format, edit the `generate_report` function in `reporting.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details