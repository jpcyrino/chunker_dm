import sys

filename = sys.argv[1]
fileout = sys.argv[2]

with open(filename, encoding="utf-8", mode="r") as file:
	lines = file.read().split("\n")

data_lines = [lines[i] for i in range(0,len(lines),3)]
print(data_lines)

with open(fileout, encoding="utf-8", mode="w") as file:
	for line in data_lines:
		file.write(line + '\n')

