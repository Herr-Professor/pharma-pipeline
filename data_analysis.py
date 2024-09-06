# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
    total_trials = len(data)
    trials_by_phase = data['Phase'].value_counts().to_dict()
    trials_by_status = data['OverallStatus'].value_counts().to_dict()
    
    # Create a pie chart of trials by phase
    plt.figure(figsize=(10, 6))
    plt.pie(trials_by_phase.values(), labels=trials_by_phase.keys(), autopct='%1.1f%%')
    plt.title('Distribution of Clinical Trials by Phase')
    plt.savefig('trials_by_phase.png')
    plt.close()

    return {
        "total_trials": total_trials,
        "trials_by_phase": trials_by_phase,
        "trials_by_status": trials_by_status
    }