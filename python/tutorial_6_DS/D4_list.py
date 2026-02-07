# Input a number and count how many times each digit (0–9) appears.

num = 67398764

counts = []
for i in range(10):
    counts.append(0)

# 0 0 0 0 0 0 0 0 0 0 -> values
# 0 1 2 3 4 5 6 7 8 9 -> index

while num>0:
    ld = num % 10       # 4
    num = num // 10     # 6739876
    
    counts[ld] = counts[ld] + 1

for i in range(10):
    if counts[i]!=0:
        print(f"{i} comes {counts[i]} times")

