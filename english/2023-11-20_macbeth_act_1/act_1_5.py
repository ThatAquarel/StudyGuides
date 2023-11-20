import random

file = open("act_1_5.csv", "r")
lines = file.readlines()

concepts = list({i.split(",")[0].upper():
				" ".join(i.split(",")[1:]).replace("\n", "")
				for i in lines
				}.items())
random.shuffle(concepts)
n = len(concepts)
results = [False for _ in range(n)]

for i, (key, value) in enumerate(concepts):
	while True:
	    response = input("%i/%i %s%s" % (i + 1, n, value, "\n>> "))

	    if response.upper() == key:
	    	print("Correct\n")
	    	break
	    elif response == "?":
	    	print("%s\n" % key)
	    results[i] = True	

n_ = n
print("Mistakes")
for i, j in enumerate(concepts):
	if results[i]:
		print("- %s" % concepts[i][0])
		n_ -= 1
print("\nResult %.2f%%" % (n_ / n * 100))