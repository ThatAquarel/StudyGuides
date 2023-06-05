import numpy as np
import pandas as pd

dates = pd.read_csv("/home/tianyi/src/StudyGuides/hqc/2023-06hqc_mees/dates.csv", sep=";")
dates = dates.sample(frac=1)

n = len(dates)
results = np.zeros(n, dtype=bool)

for i, row in dates.iterrows():
    while True:
        response = input("%i/%i %s%s" % (i + 1, n, row["EVENT"], "\n>> "))

        if row["DATE"].upper().trim() == response.upper():
            print("Correct\n")
            break
        elif response == "?":
            print("%s\n" % row["DATE"])
        results[i] = True

n_ = n
print("Mistakes")
for i, _ in dates.iterrows():
	if results[i]:
		print("- %s" % concepts[i][0])
		n_ -= 1

print("\nResult %.2f%%" % (n_ / n * 100))
