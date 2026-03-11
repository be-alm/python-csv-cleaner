import pandas as pd
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 src/clean_data.py data/sample_data.csv")
    sys.exit()

input_file = sys.argv[1]

df = pd.read_csv(input_file)

df = df.drop_duplicates()
df = df.dropna(how="all")
df.columns = df.columns.str.strip().str.lower()

filename = os.path.basename(input_file)
output_file = "cleaned_" + filename

df.to_csv(output_file, index=False)

print(f"Cleaned file saved as {output_file}")