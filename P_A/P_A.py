import sys

total = 0
lst = sys.stdin.readlines()
word = ""
for line in lst:
    for b in line:
        if b.isdigit() or (b == "-" and len(word) == 0):
            word += b
        else:
            if (word != "") and (word != "-"):
                total += int(word)
            word = ""
print(total)