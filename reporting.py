# reporting.py
def generate_report(analysis_results, search_query):
    report = f"""
Pharmaceutical Research Data Pipeline Report
===========================================

Search Query: {search_query}
Total Trials Analyzed: {analysis_results['total_trials']}

Trials by Phase:
{'-' * 20}
"""
    for phase, count in analysis_results['trials_by_phase'].items():
        report += f"{phase}: {count}\n"
    
    report += f"""
Trials by Status:
{'-' * 20}
"""
    for status, count in analysis_results['trials_by_status'].items():
        report += f"{status}: {count}\n"
    
    report += "\nA pie chart 'trials_by_phase.png' has been generated to visualize the distribution of trials by phase."
    
    with open('pipeline_report.txt', 'w') as f:
        f.write(report)
    
    print("Report generated: pipeline_report.txt")