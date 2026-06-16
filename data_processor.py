import pandas as pd
import numpy as np
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "events.csv"

def load_and_clean_data(file_path=DATA_FILE):
    # Load the ASTraM dataset
    df = pd.read_csv(file_path)
    
    # Filter for event-driven causes relevant to Theme 2
    target_causes = [
        'public_event', 'procession', 'protest', 
        'vip_movement', 'construction', 'congestion'
    ]
    df = df[df['event_cause'].isin(target_causes)].copy()
    
    # Time processing
    df['start_datetime'] = pd.to_datetime(df['start_datetime'], errors='coerce')
    df['end_datetime'] = pd.to_datetime(df['end_datetime'], errors='coerce')
    
    # Estimate duration for missing end times using the median duration of that cause
    df['duration_mins'] = (df['end_datetime'] - df['start_datetime']).dt.total_seconds() / 60
    cause_medians = df.groupby('event_cause')['duration_mins'].median()
    
    df['duration_mins'] = df.apply(
        lambda row: cause_medians.get(row['event_cause'], 120) if pd.isna(row['duration_mins']) else row['duration_mins'],
        axis=1
    )
    df['duration_mins'] = df['duration_mins'].fillna(120) # Default to 2 hours if all else fails
    
    # Extract temporal features for analysis
    df['hour'] = df['start_datetime'].dt.hour
    df['day_of_week'] = df['start_datetime'].dt.dayofweek
    df = df.dropna(subset=['latitude', 'longitude'])
    
    return df
