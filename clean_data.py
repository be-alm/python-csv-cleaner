import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: python3 clean_data.py input.csv")
    sys.exit()

input_file = sys.argv[1]

df = pd.read_csv(input_file)

df = df.drop_duplicates()
df = df.dropna(how="all")
df.columns = df.columns.str.strip().str.lower()

output_file = "cleaned_" + input_file
df.to_csv(output_file, index=False)

print(f"Cleaned file saved as {output_file}")