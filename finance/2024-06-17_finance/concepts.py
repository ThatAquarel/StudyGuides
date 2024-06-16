import random
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

file = open("concepts.csv", "r")
lines = file.readlines()

concepts = list({i.split(",")[0].upper(): " ".join(i.split(",")[1:]).replace("\n", "") for i in lines}.items())
random.shuffle(concepts)
n = len(concepts)
results = [False for _ in range(n)]

for i, (key, value) in enumerate(concepts):
    while True:
        response = input("%i/%i %s%s" % (i + 1, n, value, "\n>> "))
        similarity = similar(response.upper(), key)

        if response == "?":
            print("%s\n" % key)
        if similarity > 0.75:
            print(f"{key} {similarity:.3f}")
            print("Correct\n")
            break

        results[i] = True

n_ = n
print("Mistakes")
for i, j in enumerate(concepts):
    if results[i]:
        print("- %s" % concepts[i][0])
        n_ -= 1
print("\nResult %.2f%%" % (n_ / n * 100))
