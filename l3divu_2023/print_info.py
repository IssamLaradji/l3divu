import pandas as pd

# read meta.txt
df = pd.read_csv("meta.txt", sep="\t")

# print "Paper Title" with the "Paper ID"
for i, row in df.iterrows():
    print(f"{row['Paper ID']}: {row['Paper Title']}")
    