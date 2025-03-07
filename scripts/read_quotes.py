import pandas as pd
import random

# CSV file path
CSV_FILE = "data/movie_quotes.csv"

def get_random_quote():
    """Fetch a random movie quote from the CSV file."""
    try:
        df = pd.read_csv(CSV_FILE)

        # Select a random row
        quote_row = df.sample(n=1).iloc[0]

        # Extract the quote and movie name
        quote = quote_row['Quote']
        movie = quote_row['Movie']

        return f"🎬 {quote} \n- {movie}"

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
